from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    startingBid = models.IntegerField(default=0)
    image = models.URLField()


class Bids(models.Model):
    pass

class Comments(models.Model):
    pass

