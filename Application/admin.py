from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Organization)
admin.site.register(Practitioner)
admin.site.register(PractitionerRole)
admin.site.register(Users)
