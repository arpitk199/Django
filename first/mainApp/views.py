from django.shortcuts import render

# Create your views here.
def homePage(Request):
    return render(Request, "index.html" )

def aboutPage(Request):
    return render(Request, "about.html" )

def galleryPage(Request):
    return render(Request, "gallery.html" )

def profilePage(Request):
    return render(Request, "profile.html" )

def contactPage(Request):
    return render(Request, "contact.html" )