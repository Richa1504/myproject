from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from .models import User
from django.contrib import messages


def index(request):
    return render(request,"users/index.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = user.password  # Ideally, use Django's hashing (see next step)
            user.save()
            messages.success(request, "Registration successful!")
            return redirect("user_list")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


def user_list(request):
    users = User.objects.all()
    return render(request, "users/user_list.html", {"users": users})



def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect("user_list")

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = user.password  # Ideally, use Django's hashing (see next step)
            user.save()
            messages.success(request, "User updated successfully!")
            return redirect("user_list")
    else:
        form = RegisterForm(instance=user)
    return render(request, "users/edit_user.html", {"form": form})

