"""
Unit tests for the 'profiles' URL routing.
"""

from django.urls import resolve, reverse
from profiles.views import index, profile


def test_profiles_index_url():
    """
    Ensure the profiles index URL resolves correctly.
    """
    path = reverse('profiles_index')
    assert resolve(path).func == index


def test_profile_url():
    """
    Ensure the profile detail URL resolves correctly.
    """
    path = reverse('profile', args=["john_doe"])
    assert resolve(path).func == profile
