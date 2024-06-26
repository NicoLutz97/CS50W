from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    whishlist = models.ManyToManyField("Listing", blank=True, related_name="marked")


class Listing(models.Model):

    title = models.CharField(max_length=64, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    image = models.URLField(help_text="Insert URL for prodcut image here")
    category = models.CharField(
        max_length=64,
        default="Others",
        )
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    
    def __str__(self):
        return self.title

