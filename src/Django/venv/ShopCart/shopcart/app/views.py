from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def handler404(request):
    return render(request, '404.html')


def handler500(request):
    return render(request, '500.html')


def productList(request, prodtype):

    prods = []

    if prodtype.lower()=="books":
        book1 = {'Id':1, 'Title': 'Learn Python', 'Price': 50}
        book2 = {'Id':2, 'Title': 'Design Pattern', 'Owner': 45}
        book3 = {'Id':3, 'Title': 'ASP.NET Core', 'Owner': 39}
        prods.append(book1)
        prods.append(book2)
        prods.append(book3)
    elif  prodtype.lower()=="clothes":
        clt1 = {'Id':4, 'Title': 'Jacket', 'Price': 120}
        clt2 = {'Id':5, 'Title': 'T-shirt', 'Price': 15}
        clt3 = {'Id':6, 'Title': 'Skirt', 'Price': 30}
        prods.append(clt1)
        prods.append(clt2)
        prods.append(clt3)
    else:
        prods =[]
        # elif prodtype.lower=="toys":

    context = {'Prods': prods }

    return render(request, 'product-list.html', context)


def productCreate(request):
    return render(request, 'product-create.html')
