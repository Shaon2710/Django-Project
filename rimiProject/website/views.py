from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Student

# Create your views here.

def user_home(request):

    user=Student.objects.all()
    return render(request,"user/home.html",{
        'user':user
    })

def add_user(request):
    if request.method == "POST":
        
        user_name=request.POST.get("user_name")
        user_college=request.POST.get("user_college")
        user_age=request.POST.get("user_age")
        user_active=request.POST.get("user_active")

        user=Student()

        user.name = user_name
        user.college = user_college
        user.age = user_age
        if user_active is None:
            user.is_active = False
        else:
            user.is_active = True

        user.save()

        return redirect("/user")
    return render(request,"user/add_user.html",{})

def delete_user(request,user_id):
    duser=Student.objects.get("user_id")
    duser.delete()
    return redirect("/user")
