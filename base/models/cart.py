from django.db import models
from base.models.base import BaseEntity
from base.models.product import Product


class Cart(BaseEntity):
    products = models.ManyToManyField(Product, null=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.total
