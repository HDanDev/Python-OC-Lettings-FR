Profiles Application
====================

.. module:: profiles
   :synopsis: Django app for handling user profile data, including favorite cities.

Overview
--------

The **profiles** app handles user profile data, including favorite cities. Each profile is linked to a `User`. It includes:

- The `Profile` model, containing user-specific data
- Views for displaying and managing profile details
- URL routing for profile-related pages
- Migration history for database changes
- Unit and integration tests for validating the application logic

Models
------

.. automodule:: profiles.models.profile
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Views
-----

.. automodule:: profiles.views
   :members:
   :undoc-members:
   :show-inheritance:

URL Configuration
-----------------

.. automodule:: profiles.urls
   :members:
   :undoc-members:

.. toctree::
   :maxdepth: 1
   :caption: Migrations

   profiles.migrations


Tests
-----

The `tests/` directory includes model, URL, and view tests:

- **test_profiles_models.py** — Validates profile model creation and data integrity.
- **test_profiles_urls.py** — Verifies URL routing for profile-related pages.
- **test_profiles_views.py** — Tests page rendering for profile views.

.. rubric:: Example test (models)

.. code-block:: python

    def test_profile_model():
        user = User.objects.create_user(username="johndoe", password="password123")
        profile = Profile.objects.create(user=user, favorite_city="New York")
        assert str(profile) == "John Doe's Profile"

.. rubric:: Run with pytest:

.. code-block:: shell

    pytest profiles/tests/

