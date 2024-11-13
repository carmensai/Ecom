from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator

email_regex = RegexValidator(regex=r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', message="Please enter valid Email address.")
string_regex =  RegexValidator(regex=r'^[a-zA-Z]+(?:\s[a-zA-Z]+)*$', message="Some special characters like (~!#^`'$|{}<>*) are not allowed.")
mobile_validate = RegexValidator(regex=r'^(\+\d{1,3})?\d{10}$',message='Enter a valid 10-digit mobile number +91 9999999999')


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200,null=True,validators=[string_regex])
    user = models.OneToOneField(User, null=True, on_delete=models.SET)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class sizes(models.Model):
    size = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.size
    
class Product(models.Model):
    name = models.CharField(max_length=200,blank = True, default =None, null = True)
    description = models.CharField(max_length=400,null=True)
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    

    
class Productdetails(models.Model):
    name = models.CharField(max_length=200,null=True,validators=[string_regex])
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(max_length=6, default=0)
    size = models.ForeignKey(sizes, on_delete=models.CASCADE)
    price = models.DecimalField('price', max_digits=7, decimal_places=2, blank = True, default =None, null = True)
    def __str__(self):
        return self.name
        
class Order(models.Model):
    STATUS_REF = [
    ('Penddng','Pending'),
    ('Order Confirmed','Order Confirmed'),
    ('Out for Delivery','Out for Delivery'),
    ('Delivered','Delivered'),
    ]
    name = models.CharField(max_length=200,null=True,validators=[string_regex])
    product = models.ForeignKey( Product,null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=STATUS_REF,default= 'PENDING')
    def __str__(self):
        return self.name

class Category(models.Model): 
    name = models.CharField(max_length=50) 
  
    @staticmethod
    def get_all_categories(): 
        return Category.objects.all() 
  
    def __str__(self): 
        return self.name

class CompanyInfo(models.Model): 
    name = models.CharField(max_length=50,null=True,blank=True,default="Carmen")
    NameLine1 = models.CharField(max_length=50,validators=[string_regex])
    NameLine2 = models.CharField(max_length=50,null=True,blank=True)
    NameLine3 = models.CharField(max_length=50,null=True,blank=True)
    NameLine4 = models.CharField(max_length=50,null=True,blank=True)
    NameLine5 = models.CharField(max_length=50,null=True,blank=True)
    AddressLine1 = models.CharField(max_length=50)
    AddressLine2 = models.CharField(max_length=50,null=True,blank=True)
    AddressLine3 = models.CharField(max_length=50,null=True,blank=True)
    AddressLine4 = models.CharField(max_length=50,null=True,blank=True)
    AddressLine5 = models.CharField(max_length=50,null=True,blank=True)
    AddressCity = models.CharField(max_length=50,validators=[string_regex])
    AddressPinCode = models.CharField(max_length=50)
    AddressPhone1 = models.CharField(max_length=50,validators=[mobile_validate])
    AddressPhone2 = models.CharField(max_length=50,null=True,blank=True,validators=[mobile_validate])
    AddressEmailId = models.CharField(max_length=50,null=True,blank=True, validators=[email_regex])
    AddressCustomerCarePh = models.CharField(max_length=50,null=True,blank=True)
    LocationMapLink = models.CharField(max_length=1000,null=True,blank=True)
    YoutubeLink = models.CharField(max_length=1000,null=True,blank=True)
    FaceBookLink = models.CharField(max_length=1000,null=True,blank=True)
    InstagramLink = models.CharField(max_length=1000,null=True,blank=True)
    TwitterLink = models.CharField(max_length=1000,null=True,blank=True)
    WhatsappLink = models.CharField(max_length=1000,null=True,blank=True)
    LinkedinLink = models.CharField(max_length=1000,null=True,blank=True)
    OtherSNLink1 = models.CharField(max_length=1000,null=True,blank=True)
    OtherSNLink2 = models.CharField(max_length=1000,null=True,blank=True)
    OtherSNLink3 = models.CharField(max_length=1000,null=True,blank=True)
    SloganLine1 = models.CharField(max_length=1000,null=True,blank=True)
    SloganLine2 = models.CharField(max_length=1000,null=True,blank=True)
    SloganLine3 = models.CharField(max_length=1000,null=True,blank=True)
    LogoImage = models.ImageField(null=True,blank=True)
    def __str__(self): 
        return self.name
        
class HomepageInfo(models.Model): 
    DescriptionHeading = models.CharField(max_length=500)
    DescriptionLine1 = models.CharField(max_length=1000,null=True,blank=True)
    DescriptionLine2 = models.CharField(max_length=1000,null=True,blank=True)
    DescriptionLine3 = models.CharField(max_length=1000,null=True,blank=True)
    DescriptionImage = models.ImageField(null=True,blank=True)
    def __str__(self): 
        return self.DescriptionHeading

class AboutInfo(models.Model): 
    name = models.CharField(max_length=50,null=True,blank=True,default="Carmen")
    AboutHeadLine1 = models.CharField(max_length=1000)
    AboutHeadLine2 = models.CharField(max_length=1000,null=True,blank=True)
    AboutHeadLine3 = models.CharField(max_length=1000,null=True,blank=True)
    AboutHeadLine4 = models.CharField(max_length=1000,null=True,blank=True)
    AboutHeadLine5 = models.CharField(max_length=1000,null=True,blank=True)
    AboutDetailHead1 = models.CharField(max_length=1000)
    AboutDetailHead2 = models.CharField(max_length=1000,null=True,blank=True)
    AboutDetailHead3 = models.CharField(max_length=1000,null=True,blank=True)
    AboutDetailHead4 = models.CharField(max_length=1000,null=True,blank=True)
    AboutDetailHead5 = models.CharField(max_length=1000,null=True,blank=True)
    AboutDetailLine1 = models.CharField(max_length=1000)
    AboutDetailLine2 = models.CharField(max_length=1000,null=True,blank=True)
    AboutDetailLine3 = models.CharField(max_length=1000,null=True,blank=True)
    AboutDetailLine4 = models.CharField(max_length=1000,null=True,blank=True)
    AboutDetailLine5 = models.CharField(max_length=1000,null=True,blank=True)
    Proprietorship1 = models.CharField(max_length=1000,null=True,blank=True)
    Proprietorship2 = models.CharField(max_length=1000,null=True,blank=True)
    AboutLogoImage = models.ImageField(null=True,blank=True)
    def __str__(self): 
        return self.name

class FeedbackInfo(models.Model): 
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    name = models.CharField(max_length=50,null=True,blank=True,default="Carmen")
    email = models.CharField(max_length=50,null=True,blank=True, validators=[email_regex])
    phone = models.CharField(max_length=50,null=True,blank=True,validators=[mobile_validate])
    is_Satisfied = models.BooleanField(choices=BOOL_CHOICES)
    def __str__(self): 
        return self.name