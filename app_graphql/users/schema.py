import graphene
from users.models import User
from users.types import UserType, PermissionGroupType, PermissionType
from users.mutations.create_user import CreateUser
from users.mutations.update_user import UpdateUser
from users.mutations.delete_user import DeleteUser

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.ID(required=True))

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()