from django.shortcuts import render

# Create your views here.

def homePage(Request):
    return render(Request,"index.html")

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

def loginPage(Request):
    return render(Request,"login.html")

def shopPage(Request):
    return render(Request,"shop.html")

def singleProductPage(Request):
    return render(Request,"single-product.html")
