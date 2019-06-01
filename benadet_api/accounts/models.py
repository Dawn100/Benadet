import uuid
from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    role_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role_name = models.CharField(max_length=100)


class User(User):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=False)
    roles = models.ManyToManyField(Role)
