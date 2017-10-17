from django import forms
from app.models import ProductType, Product

class ProductForm(forms.ModelForm):
    # Id=forms.IntegerField(label='Id',required=False)
    ProdType=forms.ModelChoiceField(label="Prod Type",queryset=ProductType.objects.all(),to_field_name="" ,required=True)    
    # Title = forms.CharField(label='Title', max_length=100, required=True)
    # Price=forms.IntegerField(label='Price',required=True)

    class Meta:
        model = Product
        fields = ['Id', 'ProdType', 'Title' , 'Price']
        # exclude = ['Id']
    