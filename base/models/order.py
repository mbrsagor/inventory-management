from django.db import models

from base.models.base import BaseEntity
from base.models.product import Product


# order by user
class Order(BaseEntity):
    full_name = models.CharField(max_length=60, blank=True, null=True)
    phn_number = models.CharField(max_length=14, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.full_name}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


# order Item list
class OrderItem(BaseEntity):
    orderItem = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    products = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
