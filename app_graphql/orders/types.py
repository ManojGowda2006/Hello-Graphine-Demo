import graphene
import orders.models as Orders

class OrderType(graphene.ObjectType):
    id = graphene.ID()
    order_id = graphene.String()
    order_date = graphene.DateTime()
    order_total = graphene.Float()
    order_status = graphene.String()
