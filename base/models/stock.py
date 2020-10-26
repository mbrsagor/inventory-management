from django.db import models

from base.models.base import BaseEntity


class Stock(BaseEntity):
    name = models.CharField(max_length=90)
