"""
Main views for the 'oc_lettings_site' project.

Includes the homepage and any project-wide views.
"""

import logging
import sentry_sdk

from django.shortcuts import render
from django.http import HttpResponseServerError

logger = logging.getLogger(__name__)


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
# pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna,
# non finibus neque cursus id.
def index(request):
    """
    Display the homepage.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered homepage.
    """
    try:
        logger.info("Rendering homepage...")
        return render(request, 'index.html')

    except Exception as e:
        logger.error("Error rendering homepage: %s", str(e), exc_info=True)
        sentry_sdk.capture_exception(e)
        return HttpResponseServerError("An error occurred while rendering the homepage.")
