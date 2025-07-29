from django.shortcuts import render,redirect

from .models import DareExchange
# Create your views here.

from django.contrib.auth.models import User 
def home(request):
    dares=DareExchange.objects.all()

    print(dares)
    return render(request,"home/home.html")
#creating dare
def create_dare(request):

    if request.method == "POST":
      

        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_phone_number = request.POST.get("phone_number")
        user_deadline = request.POST.get("deadline")
        user_dare = request.POST.get("dare")
        
        
  #==========================Creating an object======================================================
        new_dare = DareExchange.objects.create(
            name = user_name,
            email = user_email,
            phone_number=user_phone_number,
            deadline=user_deadline,
            dare=user_dare
        )
        new_dare.save()
        print("new dare added successfully")


        return redirect("dares")

    return render(request, "home/create_dare.html")


#=======================Dares============================

def dares(request):

    all_dares = DareExchange.objects.all()

    return render(request, "home/dares.html",{"dares": all_dares})


#===========================Delete a Dare==================

def delete_dare(request, id):
    dare = DareExchange.objects.get(id = id)
    dare.delete()

    return redirect("dares")

#=================================Edit Dare========================
def edit_dare(request, id):
    dare = DareExchange.objects.get(id=id)

    if request.method == "POST":
       
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_phone_number = request.POST.get("phone_number")
        user_deadline = request.POST.get("deadline")
        user_dare = request.POST.get("dare")

    
        dare.name = user_name
        dare.email = user_email
        dare.phone_number = user_phone_number
        dare.deadline = user_deadline
        dare.dare = user_dare

        dare.save()
        return redirect("dares")  

   
    parameters = {
        "dare": dare
    }
    return render(request, "home/edit_dare.html", parameters)
