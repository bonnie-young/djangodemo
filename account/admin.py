from __future__ import unicode_literals
from .models import User
from django.contrib import admin


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'name', 'role')

admin.site.register(User, UserAdmin)