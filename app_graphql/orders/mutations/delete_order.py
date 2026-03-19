import graphene
from orders.models import Order
from orders.types import OrderType

class DeleteOrder(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    order = graphene.Field(OrderType)

    def mutate(self, info, id):
        order = Order.objects.get(pk=id)
        order.delete()
        return DeleteOrder(order=order)