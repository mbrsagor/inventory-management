from django.db import models
from base.models.base import BaseEntity
from django.contrib.auth.modles import User


class Customer(BaseEntity):
    owner = models.OneToOneField(User, related_name='customers')
    phone_number = models.CharField(max_length=14, unique=True)
    shop_name = models.CharField(max_length=90, unique=True)
    nid_number = models.IntegerField(max_length=20, unique=True)
    trea_liance = models.CharField(max_length=50, unique=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='customer/%Y/%m/%d', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.shop_name[:15]
   
