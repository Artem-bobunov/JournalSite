from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Journal, TechnicalError
"""
# Register your models here.
class journalAdmnin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display_list = ('npp')

class TechicalErrorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display_list = ('npp')

admin.site.register(Journal,journalAdmnin)
admin.site.register(TechnicalError,TechicalErrorAdmin)"""