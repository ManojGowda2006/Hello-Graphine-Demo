import graphene
from django.db.models import QuerySet


class OrderSortField(graphene.Enum):
    CREATED_AT = "CREATED_AT"
    STATUS = "STATUS"


class OrderSortingInput(graphene.InputObjectType):
    field = graphene.NonNull(OrderSortField)
    ascending = graphene.Boolean(default_value=True)


def apply_order_sorting(qs: QuerySet, sort_by: OrderSortingInput | None) -> QuerySet:
    if not sort_by:
        return qs

    field = sort_by.field
    direction = "" if sort_by.ascending else "-"

    if field == OrderSortField.CREATED_AT:
        return qs.order_by(f"{direction}created_at")
    if field == OrderSortField.STATUS:
        return qs.order_by(f"{direction}status")

    return qs
