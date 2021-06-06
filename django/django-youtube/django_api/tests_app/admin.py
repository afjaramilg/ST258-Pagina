from django.contrib import admin
from .models import test_model, ModelX
# Register your models here.

admin.site.register(test_model)
admin.site.register(ModelX)