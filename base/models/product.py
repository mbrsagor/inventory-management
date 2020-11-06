from django.db import models

from base.models.base import BaseEntity
from base.models.category import Category


class Product(BaseEntity):
    title = models.CharField(max_length=180)
    description = models.TextField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
