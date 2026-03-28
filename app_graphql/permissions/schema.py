import graphene
from django.db.models import Q

from permissions.models import Permission, PermissionGroup
from .types import PermissionType, PermissionGroupType
from .mutations.create_permission import CreatePermission
from .mutations.create_permission_group import CreatePermissionGroup


class Query(graphene.ObjectType):
    permission_groups = graphene.List(
        PermissionGroupType,
        search=graphene.String(),
        first=graphene.Int(),
    )
    permission_group = graphene.Field(PermissionGroupType, id=graphene.ID(required=True))
    permissions = graphene.List(
        PermissionType,
        search=graphene.String(),
        first=graphene.Int(),
    )
    permission = graphene.Field(PermissionType, id=graphene.ID(required=True))

    def resolve_permission_groups(self, info, search=None, first=None):
        queryset = PermissionGroup.objects.all().order_by("id")
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )
        if first is not None and first > 0:
            queryset = queryset[:first]
        return queryset

    def resolve_permission_group(self, info, id):
        return PermissionGroup.objects.get(pk=id)

    def resolve_permissions(self, info, search=None, first=None):
        queryset = Permission.objects.select_related("permission_group").order_by("id")
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search)
                | Q(description__icontains=search)
                | Q(permission_group__name__icontains=search)
            )
        if first is not None and first > 0:
            queryset = queryset[:first]
        return queryset

    def resolve_permission(self, info, id):
        return Permission.objects.select_related("permission_group").get(pk=id)


class Mutation(graphene.ObjectType):
    create_permission_group = CreatePermissionGroup.Field()
    create_permission = CreatePermission.Field()
