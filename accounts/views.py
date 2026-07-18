from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        else:

            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")