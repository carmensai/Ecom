from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 

class createorderform(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        exclude=['status']

class createproductform(ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class createproductdetailsform(ModelForm):
    class Meta:
        model=Productdetails
        fields='__all__'

class createsizesform(ModelForm):
    class Meta:
        model=sizes
        fields='__all__'
        exclude=['user']
        
class createcustomerform(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']

class createcategoryform(ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        exclude=['user']
        
class createcompanyinfoform(ModelForm):
    class Meta:
        model=CompanyInfo
        fields='__all__'
        exclude=['user']
        
class createhomepageinfoform(ModelForm):
    class Meta:
        model=HomepageInfo
        fields='__all__'
        exclude=['user']

class createaboutinfoform(ModelForm):
    class Meta:
        model=AboutInfo
        fields='__all__'
        exclude=['user']
class createfeedbackinfoform(ModelForm):
    class Meta:
        model=FeedbackInfo
        fields='__all__'
        exclude=['user']