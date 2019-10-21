from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Custom User Model """

    avatar = models.ImageField(null=True)
    gender = models.CharField(max_length=10, null=True)
    bio = models.TextField(default="")
