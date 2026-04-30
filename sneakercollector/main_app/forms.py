from django import forms
from .models import Collection

class CollectingForm(forms.ModelForm):
    class Meta:
        model = Collection
        # Ensure these match the variable names in class Collection(models.Model)
        fields = ['date', 'condition']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
            ),
        }
