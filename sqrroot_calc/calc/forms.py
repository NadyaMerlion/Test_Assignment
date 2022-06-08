from django import forms
from .models import Number


class NumberForm(forms.Form):
    class Meta:
        model = Number
        fields = ('a', 'b', 'c', 'result')
