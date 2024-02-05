from django.db import models
from uuid import uuid4

# Create your models here.
class User(models.Model):
    """simple user model"""
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False, unique=True)
    age = models.IntegerField(default=18)
    text = models.TextField()
