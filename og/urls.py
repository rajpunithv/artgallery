"""
URL configuration for og project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('login', views.login, name='login'),
    path('gallery', views.gallery, name='gallery'),
    path('payments', views.payments, name='payments'),
    path('artistlogin', views.artistlogin, name='artistlogin'),
    path('customerlogin', views.customerlogin, name='customerlogin'),
    path('feedback1', views.feedback1, name='feedback1'),
    path('checkmethod',views.checkmethod,name='checkmethod'),
    path('creditcard/', views.creditcard, name='creditcard'),
    path('debitcard/', views.debitcard, name='debitcard'),
    path('qrcode/', views.qrcode, name='qrcode'),
    path('cod/', views.cod, name='cod'),


    path("",include('customer.urls')),
    path("", include('artist.urls')),
    # path("",include('payments.urls')),
]
