from django.contrib import admin

from .models import Competitions, Teams, Players
# Register your models here.

admin.site.register(Competitions)
admin.site.register(Teams)
admin.site.register(Players)