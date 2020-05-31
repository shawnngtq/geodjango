from django.contrib.gis import admin

from .models import WorldBorder

# Register your models here.
admin.site.register(WorldBorder, admin.GeoModelAdmin)

"""https://code.djangoproject.com/ticket/31611"""
# admin.site.register(WorldBorder, admin.OSMGeoAdmin)
