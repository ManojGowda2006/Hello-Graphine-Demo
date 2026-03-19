import graphene
import orders.models as Orders
from orders.types import OrderType
import orders.mutations.create_order as CreateOrder
import orders.mutations.update_order as UpdateOrder
import orders.mutations.delete_order as DeleteOrder

class Query(graphene.ObjectType):
    orders = graphene.List(OrderType)
    order = graphene.Field(OrderType, id=graphene.ID(required=True))

    def resolve_orders(self, info):
        return Orders.Order.objects.all()

    def resolve_order(self, info, id):
        return Orders.Order.objects.get(pk=id)

class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    delete_order = DeleteOrder.Field()