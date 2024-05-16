from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Agent)
admin.site.register(PropertyCategory)
admin.site.register(PropertyFeature)
admin.site.register(Property)
admin.site.register(PropertyImage)