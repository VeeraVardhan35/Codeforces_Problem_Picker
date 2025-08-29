# forms.py
from django import forms
from .models import Problem

class TagForm(forms.Form):
    tag = forms.ChoiceField(
        choices=Problem.TAG_CHOICES, 
        required=False,
        label="Filter by tag"
    )

class RatingRangeForm(forms.Form):
    min_rating = forms.IntegerField(
        required=False, 
        min_value=0, 
        max_value=4000,
        widget=forms.NumberInput(attrs={'placeholder': 'Min rating'})
    )
    max_rating = forms.IntegerField(
        required=False, 
        min_value=0, 
        max_value=4000,
        widget=forms.NumberInput(attrs={'placeholder': 'Max rating'})
    )