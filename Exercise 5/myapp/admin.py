from django.contrib import admin
from . import models

class dataAdmin(admin.ModelAdmin):
    list_display = ['First_Name', 'Last_Name', 'Email']

# Register your models here.
admin.site.register(models.userform, dataAdmin)