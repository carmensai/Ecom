"""OnlineShopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from website.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.shortcuts import render

 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home ,name='home'),
    path('home.html',home ,name='home'),
    path('Index.html', Index,name='Index'),
    path('about.html',about,name='about'),
    path('services.html',services,name='services'),
    path('feedback.html',feedback,name='feedback'),
    path('placeOrder/<str:i>/',placeOrder,name='placeOrder'),
    path('register.html', registerPage,name='register'),
    path('login.html', loginPage,name='login'),
    path('logout.html', logoutPage,name='logout'),
    path('register.html', registerPage,name='register'),
    path('index/', Index,name='Index.html'),
    path('about/', about,name='about.html'),
    path('services/',services,name='services.html'),
    path('feedback/',feedback,name='feedback.html'),
    path('register/', registerPage,name='register.html'),
    path('login/', loginPage,name='login.html'),
    path('Product/', addProduct,name='addProduct.html'),
    path('sizes/', sizes,name='sizes.html'),
    path('productdetails/', productdetails,name='productdetails.html'),
    path('addcategory/', addCategory,name='addCategory.html'),
    path('addCcompanyinfo/', addCompanyInfo,name='addCompanyInfo.html'),
    path('addhomepageinfo/', addHomepageInfo,name='addHomepageInfo.html'),
    path('addaboutinfo/', addAboutInfo,name='addAboutInfo.html'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
