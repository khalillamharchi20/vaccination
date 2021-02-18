from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(ville)
admin.site.register(centre_vaccination)
admin.site.register(date_vaccination)
admin.site.register(pation)
admin.site.register(Question)