from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class FarpostAd (models.Model):
    title = models.CharField(max_length=255)
    ad_id = models.IntegerField()
    author = models.CharField(max_length=255)
    views = models.IntegerField()
    position = models.IntegerField
