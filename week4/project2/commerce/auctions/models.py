from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    CHOICES_CATEGORY = [
        ("electronics", "Electronics"),
        ("fashion", "Fashion"),
        ("sports_hobbies", "Sports and Hobbies"),
        ("house_garden", "House and Garden"),
        ("books_movies_music", "Books, Movies, Music"),
        ("others", "Others"),
    ]
    

    title = models.CharField(max_length=64, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    image = models.URLField(help_text="Insert URL for prodcut image here")
    category = models.CharField(
        max_length=64,
        choices=CHOICES_CATEGORY,
        default="others",
        )
    
    def __str__(self):
        return self.title

