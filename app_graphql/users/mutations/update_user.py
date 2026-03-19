import graphene
import users.models as User
import users.types as UserType

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
    
    user = graphene.Field(UserType)

    def mutate(self, info, id, username=None, email=None, password=None):
        user = User.objects.get(pk=id)
        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.set_password(password)
        user.save()
        return UpdateUser(user=user)    
