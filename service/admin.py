from django.contrib import admin
from .models import *


class AdminTasks(admin.ModelAdmin):
    list_display = (
        'pk', 'type', 'get_sites', 'status', 'workingIntervalStart', 'workingIntervalEnd', 'dateOfCreation', 'dateOfEnd')
    list_filter = ('type', 'status')


admin.site.register(Task, AdminTasks)
admin.site.register(File)
admin.site.register(Site)
