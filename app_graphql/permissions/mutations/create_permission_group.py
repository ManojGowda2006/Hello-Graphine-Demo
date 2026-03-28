import graphene

from permissions.models import PermissionGroup
from ..types import PermissionGroupType


class CreatePermissionGroup(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    permission_group = graphene.Field(PermissionGroupType)

    def mutate(self, info, name, description=""):
        permission_group = PermissionGroup.objects.create(
            name=name,
            description=description,
        )
        return CreatePermissionGroup(permission_group=permission_group)
