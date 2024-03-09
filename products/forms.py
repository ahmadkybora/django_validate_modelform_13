from django import forms

from .models import Product
from .validators import validate_amazing

class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['price'].required = True
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].validators.append(validate_amazing)

    class Meta:
        model = Product
        fields = '__all__'

    # def clean(self):
    #     cleaned_data = super().clean()
    #     slug = cleaned_data.get('slug', '')
    #     title = cleaned_data.get('title', '')

    #     if slug != title.lower():
    #         msg = "slug and title should be same"
    #         raise forms.ValidationError(msg)
    #     return cleaned_data
    
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity > 100:
            msg = 'Quantity should be less than 100'
            raise forms.ValidationError(msg)
        return quantity