import graphene
from django.db.models import QuerySet


class OrderFilterInput(graphene.InputObjectType):
    status = graphene.String()
    user_id = graphene.ID()


def apply_order_filter(qs: QuerySet, filters: OrderFilterInput | None) -> QuerySet:
    if not filters:
        return qs

    if getattr(filters, "status", None):
        qs = qs.filter(status=filters.status)

    if getattr(filters, "user_id", None):
        qs = qs.filter(user_id=filters.user_id)

    return qs
