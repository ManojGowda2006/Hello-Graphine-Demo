import graphene
from orders.models import Order
from ..types import OrderType

class CreateOrder(graphene.Mutation):
    class Arguments:
        order_id = graphene.String(required=True)
        order_date = graphene.DateTime(required=True)
        order_total = graphene.Float(required=True)
        order_status = graphene.String(required=True)

    order = graphene.Field(OrderType)

    def mutate(self, info, order_id, order_date, order_total, order_status):
        order = Order.objects.create(
            order_id=order_id,
            order_date=order_date,
            order_total=order_total,
            order_status=order_status
        )
        return CreateOrder(order=order)