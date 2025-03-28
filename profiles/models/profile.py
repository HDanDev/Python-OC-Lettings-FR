"""
Models for the 'profiles' application.

This module defines user profiles associated with Django's built-in User model.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile.

    Attributes:
        user (User): Associated Django user.
        favorite_city (str): User's favorite city.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
