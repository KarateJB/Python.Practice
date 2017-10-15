from django import forms

class ProductForm(forms.Form):
    id=forms.IntegerField(label='Id')
    prodTypeId=forms.IntegerField(label='ProdTypeId')    
    title = forms.CharField(label='Title', max_length=100)
    id=forms.IntegerField(label='Price')
    