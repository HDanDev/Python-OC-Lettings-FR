"""
Views for the 'lettings' application.

Handles displaying lists of lettings and details of specific rental listings.
"""

from django.shortcuts import render
from .models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum,
# consectetur quis velit. Sed non placerat massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci
# luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Display the list of all lettings.

    Args:
        request: HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page with the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta
# nisl id eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu,
# vitae efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor,
# est ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna.
# Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo
# mattis ullamcorper ac non tellus. In tristique mauris eu velit fermentum,
# tempus pharetra est luctus. Vivamus consequat aliquam libero, eget bibendum lorem.
# Sed non dolor risus. Mauris condimentum auctor elementum. Donec quis nisi ligula.
# Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    Display the details of a specific letting.

    Args:
        request: HTTP request object.
        letting_id (int): ID of the letting.

    Returns:
        HttpResponse: Rendered HTML page with letting details.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)
