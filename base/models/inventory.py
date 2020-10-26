from django.db import models

from base.models.base import BaseEntity
from base.models.category import Category
from base.models.tag import Tag


class Inventory(BaseEntity):
    name = models.CharField(max_length=120)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productCategory')
    short_description = models.CharField(max_length=250)
    full_description = models.TextField()
    current_stock = models.IntegerField(default=0)
    purchase_price = models.IntegerField(default=0)
    sales_price = models.IntegerField(default=0)
    promotional_price = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True, related_name='inventory_tag')
    picture = models.ImageField(upload_to='inventory/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name
