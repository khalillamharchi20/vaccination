from django.contrib import admin

# Register your models here.

from .models import individue,Question
admin.site.register(individue)
admin.site.register(Question)