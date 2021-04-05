from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('flux')
        else:
            messages.info(request, "Nom d'utilisateur ou mot de passe incorrect")
    context = {}
    return render(request, 'home.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Le compte a été créé au nom de :" + user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'createaccount.html', context)


def modify_account(request, id_user):
    context = {'id_user': id_user}
    return render(request, 'modifyaccount.html')
