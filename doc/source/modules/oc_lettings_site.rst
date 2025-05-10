OC Lettings Site
================

.. module:: oc_lettings_site
   :synopsis: Main project-level app for OC Lettings, handling global routing, views, templates, and error pages.

Overview
--------

The ``oc_lettings_site`` app provides the central configuration and root views for the OC Lettings project. It serves as the project's entry point, managing top-level URLs, rendering the homepage, and custom error handling pages (404, 500). It also briefly held legacy models before their migration into modular apps.

URLs
----

.. automodule:: oc_lettings_site.urls
   :members:
   :undoc-members:
   :show-inheritance:

This module includes routing to:
- Homepage (`/`)
- Lettings app (`/lettings/`)
- Profiles app (`/profiles/`)
- Django admin panel (`/admin/`)

Views
-----

.. automodule:: oc_lettings_site.views
   :members:
   :undoc-members:
   :show-inheritance:

Includes the `index` view which renders the homepage with logging and error handling via Sentry.

Templates
---------

**base.html** — Main layout template with responsive navbar, footer, and styling via Bootstrap and AOS.  
**index.html** — Homepage with introductory text and links to Lettings and Profiles.  
**404.html** — Custom 404 error page with user-friendly message and link back to home.  
**500.html** — Custom 500 error page indicating server issues and prompting retry.

Tests
-----

.. automodule:: oc_lettings_site.tests.test_views
   :members:
   :undoc-members:

.. automodule:: oc_lettings_site.tests.test_integration
   :members:
   :undoc-members:

- `test_views.py` checks homepage renders correctly.
- `test_integration.py` simulates site navigation and ensures all major pages render successfully.

.. toctree::
   :maxdepth: 1
   :caption: Migrations

   oc_lettings_site.migrations

App Configuration
-----------------

.. automodule:: oc_lettings_site.apps
   :members:
   :undoc-members:
