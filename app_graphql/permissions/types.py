import graphene


class PermissionGroupType(graphene.ObjectType):
    id = graphene.ID()
    permission_group_id = graphene.UUID()
    name = graphene.String()
    description = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()


class PermissionType(graphene.ObjectType):
    id = graphene.ID()
    permission_id = graphene.UUID()
    permission_group = graphene.Field(PermissionGroupType)
    name = graphene.String()
    description = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()
