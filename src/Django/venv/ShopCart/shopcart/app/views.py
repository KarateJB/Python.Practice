from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from app.models import Product
from share.enum import ProductTypeEnum

from app.forms.productForm import ProductForm
# Create your views here.


def home(request):
    return render(request, 'index.html')


def handler404(request):
    return render(request, '404.html')


def handler500(request):
    return render(request, '500.html')


def productList(request, prodtype):

    prods = []

    print('ProdType=' + prodtype)

    prodtypeEnum = ProductTypeEnum[prodtype]
    prods = Product.objects.filter(ProdTypeId=prodtypeEnum.value)
    # book1 = {'Id': 1, 'Title': 'Learn Python', 'Price': 50}
    # book2 = {'Id': 2, 'Title': 'Design Pattern', 'Owner': 45}
    # prods.append(book1)
    # prods.append(book2)

    context = {'Prods': prods}

    return render(request, 'product-list.html', context)


def productCreate(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        # form = ProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            entity = form.save(commit=False)
            entity.save()
            prodtypeStr = str(form.cleaned_data["ProdTypeId"].Name.lower())
            print(prodtypeStr)
            prodtypeEnum = ProductTypeEnum[prodtypeStr]
            return HttpResponseRedirect(reverse('productList', args=[prodtypeEnum.name.lower()]))
        else:
            pass
    else:
        form = ProductForm()

    return render(request, 'product-create.html', {'form': form})


def productRemove(request):

    prodtypeEnum = ProductTypeEnum.book # Default
    print('Remove')

    if request.method == 'POST':
        prodId = request.POST.get("Id", 0)
        entity = Product.objects.filter(Id=prodId).first()
        if entity is not None:
            prodtypeEnum = ProductTypeEnum[entity.ProdTypeId.Name.lower()]
            entity.delete()
    else:
        pass
       
    return HttpResponseRedirect(reverse('productList', args=[prodtypeEnum.name.lower()]))
