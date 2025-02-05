from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Signup View


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signupAdmin")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("signupAdmin")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("signupAdmin")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Signup successful! Please log in.")
        return redirect("loginAdmin")

    return render(request, "admin/authe/signupAdmin.html")


# Login View

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
      

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            request.session['username'] = username
            name = user.first_name
            request.session['name'] = name
            return redirect("indexAdmin")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("loginAdmin")

    return render(request, "admin/authe/loginAdmin.html")


# Logout View

def logout_view(request):
    request.session.flush()
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("loginAdmin")



