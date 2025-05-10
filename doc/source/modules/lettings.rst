Lettings Application
====================

.. module:: lettings
   :synopsis: Django app for managing rental listings and their addresses.

Overview
--------

The **lettings** app handles rental properties and their associated addresses. It includes:

- Two data models: `Letting` and `Address`
- Views for listing and displaying details of lettings
- Admin registration
- Synchronized migration history
- Unit and integration tests

Models
------

.. automodule:: lettings.models.address
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

.. automodule:: lettings.models.letting
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:

Views
-----

.. automodule:: lettings.views
   :members:
   :undoc-members:
   :show-inheritance:


URL Configuration
-----------------

.. automodule:: lettings.urls
   :members:
   :undoc-members:


Application Configuration
-------------------------

.. automodule:: lettings.apps
   :members:
   :undoc-members:

.. toctree::
   :maxdepth: 1
   :caption: Migrations

   lettings.migrations

Tests
-----

The `tests/` directory includes model, URL, and view tests:

- **test_lettings_models.py** — Validates model creation and string representations.
- **test_lettings_urls.py** — Verifies URL routing.
- **test_lettings_views.py** — Tests page rendering for index and detail views.

.. rubric:: Example test (models)

.. code-block:: python

    def test_letting_model():
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

.. rubric:: Run with pytest:

.. code-block:: shell

    pytest lettings/tests/


Templates
---------

HTML templates are stored in:

- `templates/lettings/index.html`
- `templates/lettings/letting.html`

They render list/detail views of `Letting` instances and extend `base.html`.

Navigation buttons and layout are built using Bootstrap-style classes.

