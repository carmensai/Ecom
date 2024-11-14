from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    products = Product.objects.all()
    CompanyInfos = CompanyInfo.objects.all()
    HomepageInfos = HomepageInfo.objects.all()
    AboutInfos = AboutInfo.objects.all()
    context = {
        'products':products,
        'CompanyInfos': CompanyInfos,
        'HomepageInfos': HomepageInfos,
        'AboutInfos': AboutInfos,
    }
    return render(request,'website/home.html',context)

def Index(request):
    products = Product.objects.all()
    CompanyInfos = CompanyInfo.objects.all()
    HomepageInfos = HomepageInfo.objects.all()
    AboutInfos = AboutInfo.objects.all()
    context = {
        'products':products,
        'CompanyInfos': CompanyInfos,
        'HomepageInfos': HomepageInfos,
        'AboutInfos': AboutInfos,
    }
    return render(request,'website/Index.html',context)
    
def about(request):
    products = Product.objects.all()
    CompanyInfos = CompanyInfo.objects.all()
    HomepageInfos = HomepageInfo.objects.all()
    AboutInfos = AboutInfo.objects.all()
    context = {
        'products':products,
        'CompanyInfos': CompanyInfos,
        'HomepageInfos': HomepageInfos,
        'AboutInfos': AboutInfos,
    }
    return render(request,'website/about.html',context)

def services(request):
    products = Product.objects.all()
    CompanyInfos = CompanyInfo.objects.all()
    HomepageInfos = HomepageInfo.objects.all()
    AboutInfos = AboutInfo.objects.all()
    context = {
        'products':products,
        'CompanyInfos': CompanyInfos,
        'HomepageInfos': HomepageInfos,
        'AboutInfos': AboutInfos,
    }
    return render(request,'website/services.html',context)
    

      
def placeOrder(request,i):
    customer= Customer.objects.get(id=i)
    form=createorderform(instance=customer)
    if(request.method=='POST'):
        form=createorderform(request.POST,instance=customer)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'website/placeOrder.html',context)


def addProduct(request):
    form=createproductform()
    if(request.method=='POST'):
        form=createproductform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'website/addProduct.html',context)

def sizes(request):
    form=createsizesform()
    if(request.method=='POST'):
        form=createsizesform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'website/sizes.html',context)

def productdetails(request):
    products = Product.objects.all()
    CompanyInfos = CompanyInfo.objects.all()
    HomepageInfos = HomepageInfo.objects.all()
    AboutInfos = AboutInfo.objects.all()
    sizes = AboutInfo.objects.all()
    form=createproductdetailsform()
    if(request.method=='POST'):
        form=createproductdetailsform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={
        'form':form,
        'customerform':customerform,
        'products':products,
        'CompanyInfos': CompanyInfos,
        'HomepageInfos': HomepageInfos,
        'AboutInfos': AboutInfos,
        'sizes': sizes,
    }
    return render(request,'website/productdetails.html',context)

def registerPage(request):
    products = Product.objects.all()
    CompanyInfos = CompanyInfo.objects.all()
    HomepageInfos = HomepageInfo.objects.all()
    AboutInfos = AboutInfo.objects.all()
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        customerform=createcustomerform()
        if request.method=='POST':
            form=createuserform(request.POST)
            customerform=createcustomerform(request.POST)
            if form.is_valid() and customerform.is_valid():
                user=form.save()
                customer=customerform.save(commit=False)
                customer.user=user 
                customer.save()
                return redirect('login')
        context={
            'form':form,
            'customerform':customerform,
            'products':products,
            'CompanyInfos': CompanyInfos,
            'HomepageInfos': HomepageInfos,
            'AboutInfos': AboutInfos,
        }
        return render(request,'website/register.html',context)

def loginPage(request):
    products = Product.objects.all()
    CompanyInfos = CompanyInfo.objects.all()
    HomepageInfos = HomepageInfo.objects.all()
    AboutInfos = AboutInfo.objects.all()
    if request.user.is_authenticated:
        return redirect('/')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={
            'login':login,
            'products':products,
            'CompanyInfos': CompanyInfos,
            'HomepageInfos': HomepageInfos,
            'AboutInfos': AboutInfos,
        }
       return render(request,'website/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')

def addCategory(request):
    form=createcategoryform()
    if(request.method=='POST'):
        form=createcategoryform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'website/addCategory.html',context)

def addCompanyInfo(request):
    form=createcompanyinfoform()
    if(request.method=='POST'):
        form=createcompanyinfoform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    context = {'donations':donations}
    return render(request,'website/addCompanyInfo.html',context)

def addHomepageInfo(request):
    form=createhomepageinfoform()
    if(request.method=='POST'):
        form=createhomepageinfoform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'website/addHomepageInfo.html',context)
    
def addAboutInfo(request):
    form=createaboutinfoform()
    if(request.method=='POST'):
        form=createaboutinfoform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'website/addAboutInfo.html',context)
    
def feedback(request):
    products = Product.objects.all()
    CompanyInfos = CompanyInfo.objects.all()
    HomepageInfos = HomepageInfo.objects.all()
    AboutInfos = AboutInfo.objects.all()
    FeedbackInfos = FeedbackInfo.objects.all()     
    feedbackform=createfeedbackinfoform()
    if request.method=='POST':
        feedbackform=createfeedbackinfoform(request.POST)
        if feedbackform.is_valid():
            feedback=feedbackform.save(commit=False)
            feedback.save()
            return redirect('home')
    context={
        'feedbackform':feedbackform,
        'products':products,
        'CompanyInfos': CompanyInfos,
        'HomepageInfos': HomepageInfos,
        'AboutInfos': AboutInfos,
        'FeedbackInfos': FeedbackInfos,
    }
    return render(request,'website/feedback.html',context)

