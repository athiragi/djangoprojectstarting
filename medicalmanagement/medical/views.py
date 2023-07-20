from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import Product,Order
# Create your views here.
def userlogin(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pwd=request.POST.get("pass1")
        user=authenticate(username=uname,password=pwd)
        if user is  not None:
            login(request,user)
            return redirect("/")
        else:
            return redirect("/login")
    return render(request,"login.html")
def signup(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        pass1=request.POST.get("pass1")
        cpass=request.POST.get("pass2")
        if(pass1 != cpass):
            return redirect("/signup")
        try:
            if User.objects.get(username=uname):
                return redirect("/signup")
        except:
            pass

        user=User.objects.create_user(uname,email,pass1)
        user.first_name=fname
        user.last_name=lname
        user.save()
        return redirect("/login")
    return render(request,"signup.html")
def home(request):
    return render(request,"home.html")
def Medicine(request): 
    pro=Product.objects.all() 
    return render(request,'productview.html',{'medical':pro}) 
def myOrder(request):
    mypro=Product.objects.all()
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        item=request.POST.get("items")
        quan=request.POST.get("quantity")
        address=request.POST.get("address")
        phon=request.POST.get("num")
        price=""
        for i in  mypro:
            if item == i.name:
                price=i.price
            pass
        newprice=int(price)*int(quan)
        user=Order(name=name,email=email,items=item,address=address,quantity=quan,phoneno=phon,price=newprice)
        user.save()
        return redirect("/myord")
    return render(request,"order.html",{'mypro':mypro})
def orderview(request):
    o=Order.objects.all()
    return render(request,"orderdeta.html",{'medsys':o})
def orderdelete(request,id):
    u=Order.objects.get(id=id)
    u.delete()
    return redirect("/myord")
