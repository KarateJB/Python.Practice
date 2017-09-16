from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')

def handler404(request):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')
