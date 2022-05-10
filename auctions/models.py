from django.contrib.auth.models import AbstractUser
from django.db import models
from numpy import minimum
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=400)
    starting_bid = models.FloatField(
        validators=MinValueValidator(0.0)
    )
    categ = models.CharField(max_length=64)


class Bid(models.Model):
    pass

class Comment(models.Model):
    pass