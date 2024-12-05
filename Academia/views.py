from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Treino

def login_view(request):


    if request.method == 'POST':
        username = request.POST['username']  # 'username' ao inves de e-mail por preguiça mesmo
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home view
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'registration/login.html')


def home(request):
    return render(request, 'home.html')

def register(request):
    # Registration logic
    return render(request, 'register.html')

@login_required
def user_page(request):
    treinos = Treino.objects.filter(usuario=request.user)
    return render(request, 'usuario.html', {'treinos': treinos})

@login_required
def adicionar_treino(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        Treino.objects.create(usuario=request.user, nome=nome, descricao=descricao)
    return redirect('user_page')