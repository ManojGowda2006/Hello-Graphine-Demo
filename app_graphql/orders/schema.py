import graphene
import orders.models as Orders
from .types import OrderType
from .mutations.create_order import CreateOrder
from .mutations.update_order import UpdateOrder
from .mutations.delete_order import DeleteOrder
from .filters import OrderFilterInput, apply_order_filter
from .sorter import OrderSortingInput, apply_order_sorting

class Query(graphene.ObjectType):
    orders = graphene.List(
        OrderType,
        filters=OrderFilterInput(),
        sort_by=OrderSortingInput(),
    )
    order = graphene.Field(OrderType, id=graphene.ID(required=True))

    def resolve_orders(self, info, filters=None, sort_by=None):
        queryset = Orders.Order.objects.all()
        queryset = apply_order_filter(queryset, filters)
        queryset = apply_order_sorting(queryset, sort_by)
        return queryset

    def resolve_order(self, info, id):
        return Orders.Order.objects.get(pk=id)

class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    delete_order = DeleteOrder.Field()