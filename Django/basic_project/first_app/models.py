from django.db import models
from uuid import uuid4

# Create your models here.

class User(models.Model):
    """model for user table"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"User: {self.id} {self.name}"


class Topic(models.Model):
    """model for user topics"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topics")
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"Topic: {self.name}"
