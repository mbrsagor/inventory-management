from django import forms
from django.forms import TextInput

from base.models.tag import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
        }
