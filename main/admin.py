from django.contrib import admin

from .models import *

admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(Client)