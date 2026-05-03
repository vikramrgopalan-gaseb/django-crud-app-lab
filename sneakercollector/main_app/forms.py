from django import forms
from .models import Collection

class CollectingForm(forms.ModelForm):
    class Meta:
        model = Collection
        # 'meal' must match the field name in your Collection model
        fields = ['date', 'meal'] 
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a Date',
                    'type': 'date'
                }
            )
        }