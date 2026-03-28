import graphene
from orders.models import Order
from ..types import OrderType

class UpdateOrder(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        order_id = graphene.String()
        order_date = graphene.DateTime()
        order_total = graphene.Float()
        order_status = graphene.String()

    order = graphene.Field(OrderType)

    def mutate(self, info, id, order_id=None, order_date=None, order_total=None, order_status=None):
        order = Order.objects.get(pk=id)

        if order_id is not None:
            order.order_id = order_id
        if order_date is not None:
            order.order_date = order_date
        if order_total is not None:
            order.order_total = order_total
        if order_status is not None:
            order.order_status = order_status

        order.save()
        return UpdateOrder(order=order)