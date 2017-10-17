from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from app.models import Product
from share.enum import ProductTypeEnum

from app.forms.productForm import ProductForm

# Create your views here.

#region Home
def home(request):
    return render(request, 'index.html')
#endregion

#region 404
def handler404(request):
    return render(request, '404.html')
#endregion

#region 500
def handler500(request):
    return render(request, '500.html')
#endregion

#region Product: List
def productList(request, prodtype):

    prods = []

    print('ProdType=' + prodtype)

    prodtypeEnum = ProductTypeEnum[prodtype]
    prods = Product.objects.filter(ProdType=prodtypeEnum.value)
    # book1 = {'Id': 1, 'Title': 'Learn Python', 'Price': 50}
    # book2 = {'Id': 2, 'Title': 'Design Pattern', 'Owner': 45}
    # prods.append(book1)
    # prods.append(book2)

    context = {'Prods': prods}

    return render(request, 'product-list.html', context)
#endregion

#region Product: Create
def productCreate(request):
    # create a form instance and populate it with data from the request:
    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        # check whether it's valid:
        if form.is_valid():
            entity = form.save(commit=False)
            entity.save()
            prodtypeStr = str(form.cleaned_data["ProdType"].Name.lower())
            prodtypeEnum = ProductTypeEnum[prodtypeStr]
            return HttpResponseRedirect(reverse('productList', args=[prodtypeEnum.name.lower()]))
        else:
            pass
    else:
        form = ProductForm()

    return render(request, 'product-create.html', {'form': form})
#endregion

#region Product: Edit
def productEdit(request, prodId):
    form = ProductForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            for cd in form.cleaned_data:
                print(cd)

            # id = form.cleaned_data["Id"] # Using will ModelForm will not get Primary key
            title = form.cleaned_data["Title"]
            price = form.cleaned_data["Price"]
            prodType = form.cleaned_data["ProdType"]

            entity = Product.objects.filter(Id=prodId).first()
            if entity is not None:
                entity.Title = title
                entity.Price = price
                entity.ProdType=prodType
                entity.save()
            else:
                pass   

            prodtypeStr = str(form.cleaned_data["ProdType"].Name.lower())
            prodtypeEnum = ProductTypeEnum[prodtypeStr]
            return HttpResponseRedirect(reverse('productList', args=[prodtypeEnum.name.lower()]))
        else:
            pass
    else:
        entity = Product.objects.filter(Id=prodId).first()
        if entity is not None:
            form = ProductForm(instance=entity)
        else:
            pass   

    return render(request, 'product-edit.html', {'form': form})
#endregion

#region Product: Remove
def productRemove(request):

    prodtypeEnum = ProductTypeEnum.book # Default

    if request.method == 'POST':
        prodId = request.POST.get("Id", 0)
        entity = Product.objects.filter(Id=prodId).first()
        if entity is not None:
            prodtypeEnum = ProductTypeEnum[entity.ProdType.Name.lower()]
            entity.delete()
    else:
        pass
       
    return HttpResponseRedirect(reverse('productList', args=[prodtypeEnum.name.lower()]))
#endregion