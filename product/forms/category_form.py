from django import forms
from django.forms import TextInput, Select, FileInput, BooleanField
from product.models.category import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'parent': Select(attrs={'class': 'form-control'}),
            'category_image': FileInput(attrs={'class': 'custom-file-input', 'id': 'imageUpload'}),
            'is_active': BooleanField()
        }
