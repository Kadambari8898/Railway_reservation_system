from django.shortcuts import render
from .models import booking, contact, home






def func0(request):
    if request.method=="POST":
        home_obj=home()
        home_obj.email=request.POST.get("email")
        home_obj.email=request.POST.get("password")
        home_obj.save()
        return render(request,"Tejas_App/signup.html")
    
    else:
         return render(request,"Tejas_App/Home.html")


def func(request):
    return render(request,"Sample.html")

def func1(request):
    return render(request,"Tejas_App/Sample.html")

def func5(request):
    if request.method=='POST':
        booking_obj=booking()
        booking_obj.firstname=request.POST.get("firstname")
        booking_obj.lastname=request.POST.get("lastname")
        booking_obj.email=request.POST.get("email")
        booking_obj.From=request.POST.get("from")
        booking_obj.to=request.POST.get("to")
        booking_obj.save()
        return render(request,"Tejas_App/signup.html")
    else:
         return render(request,"Tejas_App/Home.html")

def fun6(request):
    return render(request,"Tejas_App/index.html")

def func2(request):
    if request.method=='POST':
        contact_obj=contact()
        contact_obj.name=request.POST.get("name")
        contact_obj.email=request.POST.get("email")
        contact_obj.desc=request.POST.get("desc")
        contact_obj.save()
        return render(request,"Tejas_App/Home.html") 


    else:
        return render(request,"Tejas_App/sample2.html")

    

    

def fun3(request):
        booking1=booking.objects.all()
        return render(request,"Tejas_App/index.html",{
            'booking':booking1
        })
           


def func4(request):
    return render(request,"Tejas_App/reservation.html")