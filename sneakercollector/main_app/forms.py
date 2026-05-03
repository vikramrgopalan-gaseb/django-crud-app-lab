from django import forms
from .models import Collection

class CollectingForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['date', 'condition'] 
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a Date',
                    'type': 'date'
                }
            )
        }