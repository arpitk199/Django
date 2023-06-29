from django.shortcuts import render

# Create your views here.
def homePage(Request):
    return render(Request, "index.html" )

def aboutPage(Request):
    return render(Request, "about.html" )

def galleryPage(Request):
    return render(Request, "gallery.html" )

def profilePage(Request):
    data = [
        {"id":101,"name":"Arpit Kumar","dsg":"Engineer","salary":10000,"addres":"UP"},
        {"id":102,"name":"Amit Kumar","dsg":"Engineer","salary":20000,"addres":"UP"},
        {"id":103,"name":"Ravi Kumar","dsg":"Engineer","salary":30000,"addres":"UP"},
        {"id":104,"name":"Piyush Kumar","dsg":"Engineer","salary":10000,"addres":"UP"},
        {"id":105,"name":"Ankit Kumar","dsg":"Engineer","salary":40000,"addres":"UP"},
        {"id":106,"name":"Shivam Kumar","dsg":"Engineer","salary":50000,"addres":"UP"}
    ]
    return render(Request, "profile.html", {"data":data} )

def contactPage(Request):
    return render(Request, "contact.html", {
                                         "name":"Arpit Kumar",
                                         "email":"kumararpit199@gmail.com",
                                         "phone":"7983285628"} )