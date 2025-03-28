"""
Integration tests for the 'lettings' views.
"""

import pytest
from django.urls import reverse
from lettings.models.address import Address
from lettings.models.letting import Letting


@pytest.mark.django_db
def test_lettings_index(client):
    """
    Test the lettings index page.
    """
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200
    assert b"<h1 class=\"page-header-ui-title mb-3 display-6\">Lettings</h1>" in response.content


@pytest.mark.django_db
def test_letting_detail(client):
    """
    Test the letting detail page.
    """
    address = Address.objects.create(
        number=12,
        street="Main St",
        city="NY",
        state="NY",
        zip_code=10001,
        country_iso_code="USA"
        )
    letting = Letting.objects.create(title="Test Letting", address=address)

    response = client.get(reverse('letting', args=[letting.id]))
    assert response.status_code == 200
    assert b"<p>12 Main St</p>" in response.content
