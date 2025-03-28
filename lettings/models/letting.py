"""
Models for the 'lettings' application.

This module defines the data models related to property lettings,
including addresses and rental listings.
"""

from django.db import models
from .address import Address


class Letting(models.Model):
    """
    Represents a rental listing.

    Attributes:
        title (str): Title of the rental listing.
        address (Address): Associated address of the rental.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
