from django.db import models

from reusable.models import BaseModel


class Vocabulary(BaseModel):
    expression = models.CharField(max_length=20)
    short_description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
