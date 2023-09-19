from django.db import models
from django.contrib.auth.models import User

from .consts import (
    ACCOUNT_TIERS
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.IntegerField(choices=ACCOUNT_TIERS)


class Image(models.Model):
    image = models.ImageField()
    profile = models.ForeignKey(Profile, related_name='images', on_delete=models.CASCADE)
