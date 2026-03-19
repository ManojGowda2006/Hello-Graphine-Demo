import graphene

class UserType(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()  # Note: In production, you should never expose passwords!
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()

class PermissionGroupType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()

class PermissionType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()