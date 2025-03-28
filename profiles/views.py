"""
Views for the 'profiles' application.

Handles displaying user profiles and lists of profiles.
"""

from django.shortcuts import render
from .models import Profile


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
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


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
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
