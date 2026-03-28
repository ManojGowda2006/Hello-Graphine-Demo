import graphene
from users.models import User
from .types import UserType, PermissionGroupType, PermissionType
from .mutations.create_user import CreateUser
from .mutations.update_user import UpdateUser
from .mutations.delete_user import DeleteUser

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.ID(required=True))

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()