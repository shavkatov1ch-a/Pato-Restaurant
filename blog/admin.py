from django.contrib import admin
from .models import *


class AdminHome(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ['id', 'title']


class AdminPato(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ['id', 'title']


class AdminMenu(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ['id', 'title']


admin.site.register(Home, AdminHome)
admin.site.register(Pato, AdminPato)
admin.site.register(Menu, AdminMenu)