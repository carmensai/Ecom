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


 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home ,name='home'),
    path('index/', Index,name='Index'),
    path('about/', about,name='about'),
    path('services/',services,name='services'),
    path('feedback/',feedback,name='feedback'),
    path('home.html',home ,name='home'),
    path('Index.html', Index,name='Index'),
    path('about.html',about,name='about'),
    path('services.html',services,name='services'),
    path('feedback.html',feedback,name='feedback'),
    path('placeOrder/<str:i>/',placeOrder,name='placeOrder'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),
    path('register.html', registerPage,name='register'),
    path('addProduct/', addProduct,name='addProduct'),
    path('sizes/', sizes,name='sizes'),
    path('productdetails/', productdetails,name='productdetails'),
    path('addCategory/', addCategory,name='addCategory'),
    path('addCompanyInfo/', addCompanyInfo,name='addCompanyInfo'),
    path('addHomepageInfo/', addHomepageInfo,name='addHomepageInfo'),
    path('addAboutInfo/', addAboutInfo,name='addAboutInfo'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
