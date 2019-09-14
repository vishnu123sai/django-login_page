from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import UserDetails
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return render(request,"login.html" );
def email(request):
    if request.method == "POST":
        email = request.POST['email'];
        pwd = request.POST['password'];
        user = authenticate(request, username=email, password=pwd);
        if user is not None:
            login(request, user)
            return render(request, "success.html", context={email:email});
        else:
            return render(request, "invalid.html" );
    return render(request, "error_page.html")
    

def signup(request):
    if request.method == "POST":
        try:
            first_name = request.POST["f_name"];
            last_name = request.POST["l_name"];
            email = request.POST["email"];
            username = request.POST['email'];
            pwd = request.POST["password"];
            user = User.objects.create_user(username=username, email=email,password=pwd);
            user.last_name = last_name;
            user.first_name =first_name;
            user.save()
            return render(request, "account_created.html");
        except:
            return render(request,"account_exists.html");
    return render(request, "error_page.html")

