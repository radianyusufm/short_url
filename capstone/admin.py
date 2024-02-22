from django.contrib import admin

from .models import User, Urlshort, Analytics
# Register your models here.
admin.site.register(User)
admin.site.register(Urlshort)
admin.site.register(Analytics)