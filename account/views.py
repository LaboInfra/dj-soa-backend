from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserLogin as UserLoginForm


# Create your views here.
def login_view(request):
    if request.method == "POST":
        user_login = UserLoginForm(request.POST)
        if user_login.is_valid():
            email = user_login.cleaned_data.get("email")
            password = user_login.cleaned_data.get("password")

            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            user_login.add_error(None, "Invalid credentials")
            return render(request, "account/login.html", {"form": user_login})

    else:
        user_login = UserLoginForm()
    return render(request, "account/login.html", {"form": user_login})
