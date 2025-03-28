"""
Unit tests for the 'lettings' URL routing.
"""

from django.urls import resolve, reverse
from lettings.views import index, letting


def test_lettings_index_url():
    """
    Ensure the lettings index URL resolves correctly.
    """
    path = reverse('lettings_index')
    assert resolve(path).func == index


def test_letting_url():
    """
    Ensure the letting detail URL resolves correctly.
    """
    path = reverse('letting', args=[1])
    assert resolve(path).func == letting
