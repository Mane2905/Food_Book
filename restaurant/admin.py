from django.contrib import admin

from .models import Menu,Restaurant,Order

# Register your models here.
admin.site.register(Menu)
admin.site.register(Restaurant)
admin.site.register(Order)