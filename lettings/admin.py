from django.contrib import admin

from .models.letting import Letting
from .models.address import Address


admin.site.register(Letting)
admin.site.register(Address)
