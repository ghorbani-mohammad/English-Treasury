from django.db import models

from reusable.models import BaseModel


class Vocabulary(BaseModel):
    expression = models.CharField(max_length=20)
