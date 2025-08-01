from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):



    if request.method == "POST":
       
       
       username = request.POST.get("username")
       first_name = request.POST.get("first_name") 
       last_name=request.POST.get("last_name") 
       email=request.POST.get("email") 
       password=request.POST.get("password") 
      
       
       new_user=User.objects.create(
           username = username,
           first_name = first_name,
           last_name = last_name,
           email = email,

       )
       new_user.set_password(password)  #setting the password for the new user in an encrypted (hashed)
       new_user.save()

       return redirect("dashboard")



    return render(request,"accounts/register.html")

#=====================Login======================

def login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(request, username = username, password = password)

        if user is not None:
            auth.login(request, user)

            return redirect("dashboard")
        print("Invalid username or password")
    return render(request, "accounts/login.html")


def logout(request):
    auth.logout(request)

    return redirect("home")