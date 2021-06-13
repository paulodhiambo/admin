from django.contrib.auth.models import AbstractUser
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0)

