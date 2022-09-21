from dataclasses import fields
from . models import Todo
from django import forms

class Todoforms(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['headline']