from django import forms
from .models import Condition

class ConditionForm(forms.ModelForm):
    class Meta:
        model = Condition
        fields = ['DS', 'NDS', 'W']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a Date',
                    'type': 'date'
                }
            )
        }