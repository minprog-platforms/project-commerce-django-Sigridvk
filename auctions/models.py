from tracemalloc import start
from django.contrib.auth.models import AbstractUser
from django.db import models
from numpy import minimum
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.IntegerField(default=0)
    category = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="all_listings", default=None)
    image_url = models.URLField(max_length=400)

class Bid(models.Model):
    amount = models.IntegerField(default=0)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="all_bids", default=None)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="all_user_bids", default=None)

class Comment(models.Model):
    date = models.DateField(default=None)
    time = models.TimeField(default=None)
    comment = models.TextField(default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="all_user_comments", default=None)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="all_comments", default=None)