import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import graphene

from app_graphql.users.schema import Query as UsersQuery, Mutation as UsersMutation
from app_graphql.orders.schema import Query as OrdersQuery, Mutation as OrdersMutation
from app_graphql.permissions.schema import Query as PermissionsQuery, Mutation as PermissionsMutation


class RootQuery(UsersQuery, OrdersQuery, PermissionsQuery, graphene.ObjectType):
    pass


class RootMutation(UsersMutation, OrdersMutation, PermissionsMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)


@csrf_exempt
def graphql_view(request):
    # Support:
    # - GET without ?query= -> serve GraphQL Playground UI
    # - GET with ?query=    -> execute query (simple browser testing)
    # - POST                -> normal GraphQL clients
    if request.method == "GET":
        if "query" not in request.GET:
            api_url = request.build_absolute_uri("/graphql")
            plugins_url = request.build_absolute_uri("/plugins/")
            return render(
                request,
                "graphql/playground.html",
                {
                    "api_url": api_url,
                    "plugins_url": plugins_url,
                    "query": None,
                },
            )

        query = request.GET.get("query")
        variables_raw = request.GET.get("variables")
        variables = None
        if variables_raw:
            try:
                variables = json.loads(variables_raw)
            except json.JSONDecodeError:
                return JsonResponse(
                    {"error": "Invalid variables JSON in query string"}, status=400
                )
    elif request.method == "POST":
        try:
            payload = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)
        query = payload.get("query")
        variables = payload.get("variables")
    else:
        return JsonResponse({"error": "Only GET and POST are allowed"}, status=405)

    if not query:
        return JsonResponse({"error": "Missing 'query' parameter"}, status=400)

    # Context carries the Django request and a per-request dataloader cache.
    context = {"request": request, "loaders": {}}

    result = schema.execute(query, variable_values=variables, context_value=context)

    response_data = {}
    if result.errors:
        response_data["errors"] = [str(e) for e in result.errors]
    if result.data is not None:
        response_data["data"] = result.data

    status = 400 if result.errors else 200
    return JsonResponse(response_data, status=status)
