from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
# Register your models here.
from .models import questionBank

@admin.register(questionBank)
class questionBank1(ImportExportModelAdmin):
    exclude = ('id', )