import graphene

from permissions.models import Permission, PermissionGroup
from ..types import PermissionType


class CreatePermission(graphene.Mutation):
    class Arguments:
        permission_group_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        description = graphene.String()

    permission = graphene.Field(PermissionType)

    def mutate(self, info, permission_group_id, name, description=""):
        permission_group = PermissionGroup.objects.get(pk=permission_group_id)
        permission = Permission.objects.create(
            permission_group=permission_group,
            name=name,
            description=description,
        )
        return CreatePermission(permission=permission)
