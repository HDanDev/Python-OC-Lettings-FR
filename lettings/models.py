"""
Models for the 'lettings' application.

This module defines the data models related to property lettings, 
including addresses and rental listings.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address.
    
    Attributes:
        number (int): Street number.
        street (str): Street name.
        city (str): City name.
        state (str): Two-letter state abbreviation.
        zip_code (int): ZIP code.
        country_iso_code (str): ISO 3166-1 alpha-3 country code.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.number} {self.street}'


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
