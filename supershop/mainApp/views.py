from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.messages import success,error
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from .models import *

# Create your views here.

def homePage(Request):
    Products = Product.objects.all().order_by("-id")[0:12]
    return render(Request,"index.html",{'products':Products})

def aboutPage(Request):
    return render(Request,"about.html")

def cartPage(Request):
    return render(Request,"cart.html")

def checkoutPage(Request):
    return render(Request,"checkout.html")

def confirmationPage(Request):
    return render(Request,"confirmation.html")

def contactPage(Request):
    return render(Request,"contact.html")

def shopPage(Request,mc,sc,br):
    if(mc=="All" and sc=="All" and br=="All"):
        Products = Product.objects.all().order_by("-id")
    elif(mc!="All" and sc=="All" and br=="All"):
        Products = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by("-id")
    elif(mc=="All" and sc!="All" and br=="All"):
        Products = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
    elif(mc=="All" and sc=="All" and br!="All"):
        Products = Product.objects.filter(barnd=Brand.objects.get(name=br)).order_by("-id")
    elif(mc!="All" and sc!="All" and br=="All"):
        Products = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by("-id").order_by("-id")
    elif(mc!="All" and sc=="All" and br!="All"):
        Products = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),barnd=Brand.objects.get(name=br)).order_by("-id").order_by("-id")
    elif(mc=="All" and sc!="All" and br!="All"):
        Products = Product.objects.filter(barnd=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by("-id").order_by("-id")
    else:
         Products = Product.objects.filter(barnd=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc),maincategory=Maincategory.objects.get(name=mc)).order_by("-id").order_by("-id")


    maincategory = Maincategory.objects.all().order_by("-id")
    subcategory = Subcategory.objects.all().order_by("-id")
    brand = Brand.objects.all().order_by("-id")
    return render(Request,"shop.html",{'products':Products,'maincategory':maincategory,'subcategory':subcategory,'brand':brand,'mc':mc,'sc':sc,'br':br})

def singleProductPage(Request,id):
    product = Product.objects.get(id=id)
    return render(Request,"single-product.html",{'product':product})

def loginPage(Request):
    if(Request.method=="POST"):
        username =Request.POST.get("username")
        password =Request.POST.get("password")
        user = authenticate(username=username,password=password)
        if(user is not None):
            if(user.is_superuser):
                return HttpResponseRedirect("/admin")
            else:
                return HttpResponseRedirect("/profile")
        else:
            error(Request,"Invalid username or Password !!!")
    return render(Request,"login.html")

def signupPage(Request):
    if(Request.method=="POST"):
        password = Request.POST.get("password")
        cpassword = Request.POST.get("cpassword")
        if(password==cpassword):
            username = Request.POST.get("username")
            email = Request.POST.get("email")
            name = Request.POST.get("name")
            try:
                User.objects.create_user(username=username,email=email,password=password,first_name=name)
                phone = Request.POST.get("phone")

                b = Buyer()
                b.name = name
                b.email = email
                b.username = username
                b.phone = phone
                b.save()
                return HttpResponseRedirect("/login")
            except:
                error(Request,"username Already Exist !!!")
        else:
            error(Request,"Password and Confirm Password Doesn't Matched!!!")
    return render(Request,"signup.html")
