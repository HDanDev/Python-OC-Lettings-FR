import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_site_navigation(client):
    """
    Test browsing through the entire site and check if all pages work correctly.
    """

    # Create some sample users and profiles for the test
    user = User.objects.create(username="john_doe")
    Profile.objects.create(user=user, favorite_city="Paris")

    # Create an Address instance
    address = Address.objects.create(
        number=123,
        street="Baker Street",
        city="London",
        zip_code=56789
    )

    # Create a Letting instance and assign the Address instance to it
    letting = Letting.objects.create(title="Cozy Apartment", address=address)

    # Test Homepage (index)
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert b'Welcome to Holiday Homes' in response.content

    # Test Lettings Index
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200
    assert b'Lettings' in response.content
    assert b'Cozy Apartment' in response.content

    # Test Profile Index
    response = client.get(reverse('profiles_index'))
    assert response.status_code == 200
    assert b'Profiles' in response.content
    assert b'john_doe' in response.content

    # Test Profile Detail (user profile page)
    response = client.get(reverse('profile', args=["john_doe"]))
    assert response.status_code == 200
    assert b'john_doe' in response.content
    assert b'<p><strong>Favorite city :</strong> Paris</p>' in response.content

    # Test Letting Detail
    response = client.get(reverse('letting', args=[letting.id]))
    assert response.status_code == 200
    assert b'Cozy Apartment' in response.content
    assert b'123 Baker Street' in response.content
