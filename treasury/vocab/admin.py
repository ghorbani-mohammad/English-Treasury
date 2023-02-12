from django.contrib import admin

from . import models
from reusable.admins import ReadOnlyAdminDateFieldsMIXIN


@admin.register(models.Vocabulary)
class VocabularyAdmin(ReadOnlyAdminDateFieldsMIXIN, admin.ModelAdmin):
    list_display = ("pk", "expression", "created_at")
