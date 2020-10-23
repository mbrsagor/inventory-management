from django.db import models
from base.models.base import BaseEntity


class Category(BaseEntity):
    name = models.CharField(max_length=90, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='sub_category')
    category_image = models.ImageField(upload_to='category/%Y/%m/%d', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_children(self):
        return Category.objects.filter(parent=self)
