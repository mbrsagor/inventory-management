from django.db import models
from base.models.base import BaseEntity


class Tag(BaseEntity):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
