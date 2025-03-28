"""
Integration tests for the 'profiles' views.
"""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

@pytest.mark.django_db
def test_profiles_index(client):
    """
    Test the profiles index page.
    """
    response = client.get(reverse('profiles_index'))
    assert response.status_code == 200
    assert b"<h1 class=\"page-header-ui-title mb-3 display-6\">Profiles</h1>" in response.content

@pytest.mark.django_db
def test_profile_detail(client):
    """
    Test the profile detail page.
    """
    user = User.objects.create(username="jane_doe")
    Profile.objects.create(user=user, favorite_city="Rome")

    response = client.get(reverse('profile', args=["jane_doe"]))
    assert response.status_code == 200
    assert b"jane_doe" in response.content
