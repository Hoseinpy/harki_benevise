from django.contrib import admin
from .models import MAinPageModel

@admin.register(MAinPageModel)
class MAinPageModelAdmin(admin.ModelAdmin):
    list_display = ['text']
