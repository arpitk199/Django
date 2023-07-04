from django.shortcuts import render

# Create your views here.
def homePage(Request):
    lv = 0
    lc = 0
    uv = 0
    uc = 0
    d = 0
    s = 0
    sp = 0
    show = False
    if(Request.method=="POST"):
        show = True
        message = Request.POST.get("message")
        for i in message:
            if(i>='a' and i<='z'):
                if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
                    lv = lv + 1
                else:
                    lc = lc + 1
            elif(i>='A' and i<='Z'):
                if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                    uv = uv + 1
                else:
                    uc = uc + 1
            elif(i>='0' and i<='9'):
                d = d + 1
            elif(i==' '):
                s = s + 1
            else:
                sp = sp + 1
            
    return render(Request,"index.html",{'lv':lv,'lc':lc,'uv':uv,'uc':uc,'d':d,'s':s,'sp':sp,'show':show})

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