"""
Views for the 'profiles' application.

Handles displaying user profiles and lists of profiles.
"""

import logging
import sentry_sdk

from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponseNotFound
from .models.profile import Profile

logger = logging.getLogger(__name__)


# Sed placerat quam in pulvinar commodo.
# Nullam laoreet consectetur ex, sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque,
# quis dictum lacus d
def index(request):
    """
    Display the list of all profiles.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page with the list of profiles.
    """
    try:
        logger.info("Fetching all profiles...")
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)

    except Exception as e:
        logger.error("Error fetching profiles: %s", str(e), exc_info=True)
        sentry_sdk.capture_exception(e)  # Send error to Sentry
        return HttpResponseServerError("An error occurred while fetching profiles.")


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui.
# Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Display the details of a specific user profile.

    Args:
        request: HTTP request object.
        username (str): Username of the profile.

    Returns:
        HttpResponse: Rendered HTML page with profile details.
    """
    try:
        logger.info(f"Fetching profile for username: {username}")
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)

    except Profile.DoesNotExist:
        logger.warning(f"Profile not found: {username}")
        return HttpResponseNotFound("Profile not found.")

    except Exception as e:
        logger.error("Error fetching profile: %s", str(e), exc_info=True)
        sentry_sdk.capture_exception(e)
        return HttpResponseServerError("An error occurred while fetching the profile.")
