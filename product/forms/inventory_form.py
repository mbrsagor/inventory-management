from django import forms
from django.forms import TextInput, Select, FileInput, NumberInput, Textarea

from product.models.inventory import Inventory


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'category_name': Select(attrs={'class': 'form-control', 'id': 'category_name'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'id': 'short_description'}),
            'full_description': Textarea(attrs={'class': 'form-control', 'id': 'full_description'}),
            'current_stock': NumberInput(attrs={'class': 'form-control', 'id': 'current_stock'}),
            'purchase_price': NumberInput(attrs={'class': 'form-control', 'id': 'purchase_price'}),
            'sales_price': NumberInput(attrs={'class': 'form-control', 'id': 'sales_price'}),
            'promotional_price': NumberInput(attrs={'class': 'form-control', 'id': 'promotional_price'}),
            'picture': FileInput(attrs={'class': 'form-control', 'id': 'picture'}),
        }
