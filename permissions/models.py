from django.db import models
import uuid

class PermissionGroup(models.Model):
	permission_group_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Permission(models.Model):
	permission_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	permission_group = models.ForeignKey(
		PermissionGroup,
		on_delete=models.CASCADE,
		related_name="permissions",
	)
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
