"""shopcart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app.views import home, productList, productCreate, productRemove

# handler404 = 'app.views.http404'
# handler500 = 'app.views.http500'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^product/(?P<prodtype>\w+)/$', productList, name='productList'),
    url(r'^product/create$', productCreate, name='productCreate'),
    url(r'^product/remove$', productRemove, name='productRemove'),
    url(r'^admin/', admin.site.urls),
]
