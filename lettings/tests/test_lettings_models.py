"""
Unit tests for the 'lettings' models.
"""

import pytest
from lettings.models import Address, Letting

@pytest.mark.django_db
def test_address_model():
    """
    Test that an Address object is correctly created.
    """
    address = Address.objects.create(
        number=123,
        street="Baker Street",
        city="London",
        state="LD",
        zip_code=56789,
        country_iso_code="GBR"
    )
    assert str(address) == "123 Baker Street"

@pytest.mark.django_db
def test_letting_model():
    """
    Test that a Letting object is correctly created and associated with an Address.
    """
    address = Address.objects.create(
        number=221,
        street="Baker Street",
        city="London",
        state="LD",
        zip_code=12345,
        country_iso_code="GBR"
    )
    letting = Letting.objects.create(title="Sherlock's Home", address=address)
    
    assert str(letting) == "Sherlock's Home"
