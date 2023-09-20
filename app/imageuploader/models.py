from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from .consts import (
    ACCOUNT_TIERS
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.IntegerField(choices=ACCOUNT_TIERS, default=1)


class UserImage(models.Model):
    image = models.ImageField()
    profile = models.ForeignKey(Profile, related_name='images', on_delete=models.CASCADE)


# Create Profile when new User Signs Up
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Token.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
