"""
Integration tests for the 'oc_lettings_site' views.
"""

import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_homepage(client):
    """
    Test the homepage.
    """
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert b"<h1 class=\"page-header-ui-title mb-3 display-6\">Welcome to Holiday Homes</h1>" in response.content
