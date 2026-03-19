import graphene
import users.models as User
import users.types as UserType

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    success = graphene.Boolean()

    def mutate(self, info, id):
        user = User.objects.get(pk=id)
        user.delete()
        return DeleteUser(success=True)
