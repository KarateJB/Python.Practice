from django import forms
from app.models import ProductType

class ProductForm(forms.Form):
    id=forms.IntegerField(label='Id')
    prodTypeId=forms.ModelChoiceField(label="Prod Type",queryset=ProductType.objects.all(),to_field_name="" ,required=True)    
    title = forms.CharField(label='Title', max_length=100)
    id=forms.IntegerField(label='Price')
    
    