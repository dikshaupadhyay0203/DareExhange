from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here

@login_required
def ask_ai(request):
    if request.method == "POST":
        query = request.POST.get("query")
        response = generate_response(query)
        parameters = {
            "response": response
        }
        return render(request, "dashboard/ask_ai.html", parameters)
    return render(request, "dashboard/ask_ai.html")  # This line runs for GET requests

def dashboard(request):
    return render(request, "dashboard/index.html")

def generate_response(query):
    return "query ka response"
