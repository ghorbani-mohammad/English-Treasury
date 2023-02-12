from django.contrib import admin

from . import models


@admin.register(models.Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ("pk", "expression", "created_at")
