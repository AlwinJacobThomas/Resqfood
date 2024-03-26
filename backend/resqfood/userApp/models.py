from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_organization = models.BooleanField(default=False)
    is_individual = models.BooleanField(default=False)