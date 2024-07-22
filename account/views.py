from django.shortcuts import render
from .forms import UserLogin as UserLoginForm
from .models import User

# Create your views here.
def login(request):
    if request.method == "POST":
        user_login = UserLoginForm(request.POST)
        if user_login.is_valid():
            email = user_login.cleaned_data.get("email")
            password = user_login.cleaned_data.get("password")

            # check if user exists
            if not User.objects.filter(email=email).exists():
                user_login.add_error(None, "Invalid credentials")
                return render(request, "account/login.html", {"form": user_login})

            user = User.objects.get(email=email)
            if user.check_password(password):
                return render(request, "account/login.html", {"form": user_login})

            user_login.add_error(None, "Invalid credentials")
            return render(request, "account/login.html", {"form": user_login})

    else:
        user_login = UserLoginForm()
    return render(request, "account/login.html", {"form": user_login})
