from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class User(AbstractUser):
    """Extension of User model to add extra profile info"""

    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(Group, related_name='base_app_users', blank=True)
    user_permissions = models.ManyToManyField(Permission,
                                              related_name='base_app_users',
                                              verbose_name=('user permissions'),
                                              blank=True,
                                              help_text=('Specific permissions for this user.'),)

    portfolio_link = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',
                                    # The upload_to is used to specify the directory which you want to save
                                    # the profile pics to in your media folder
                                    # so in the case, it would be 'media/profile_pics
                                    blank=True)
    class Meta:
        app_label = 'base_app'

    def __str__(self) -> str:
        return self.username
