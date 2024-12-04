from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redireciona o usuario se ele ja estiver autentificado

    if request.method == 'POST':
        username = request.POST['username']  # 'username' ao inves de e-mail por preguiça mesmo
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home view
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')

def register(request):
    # Registration logic
    return render(request, 'register.html')

def user_page(request):
    # User page logic
    return render(request, 'user.html')