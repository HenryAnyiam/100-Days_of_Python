from django.db import models
from uuid import uuid4

# Create your models here.
class User(models.Model):
    """model for users"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
