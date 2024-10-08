from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'  # Sets email field as unique user identifier
    REQUIRED_FIELDS = []

    def __str__(self):
      return self.email
