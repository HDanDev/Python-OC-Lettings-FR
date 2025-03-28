"""
Unit tests for the 'profiles' models.
"""

import pytest
from django.contrib.auth.models import User
from profiles.models.profile import Profile


@pytest.mark.django_db
def test_profile_model():
    """
    Test that a Profile object is correctly created and linked to a User.
    """
    user = User.objects.create(username="john_doe")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    assert str(profile) == "john_doe"
