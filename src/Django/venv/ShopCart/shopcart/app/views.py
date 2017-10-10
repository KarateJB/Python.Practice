from django.shortcuts import render

# Create your views here.


def home(request):
    car1 = {'Id':1, 'Name': 'Focus', 'Owner'2: 'JB'}
    car2 = {'Id':2, 'Name': 'Lancer', 'Owner': 'Lily'}
    car3 = {'Id':3, 'Name': 'Swift', 'Owner': 'leia'}
    Cars = []
    Cars.append(car1)
    Cars.append(car2)
    Cars.append(car3)
    
    context = {'Cars': Cars }

    return render(request, 'index.html', context)

def handler404(request):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')
