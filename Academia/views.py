from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Treino, Exercicio
from datetime import timedelta

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
    treino_id = request.GET.get('treino_id')
    treino_selecionado = None
    if treino_id:
        treino_selecionado = get_object_or_404(Treino, id=treino_id, usuario=request.user)
    return render(request, 'usuario.html', {'treinos': treinos, 'treino_selecionado': treino_selecionado})

@login_required
def adicionar_treino(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        novo_treino = Treino.objects.create(usuario=request.user, nome=nome, descricao=descricao)
        messages.success(request, 'Treino criado com sucesso! Adicione exercícios ao seu treino.')
        return redirect(f'/user/?treino_id={novo_treino.id}')
    return redirect('user_page')

@login_required
def adicionar_exercicio(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id, usuario=request.user)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        repeticoes = request.POST.get('repeticoes')
        tempo_descanso_str = request.POST.get('tempo_descanso')
        peso = request.POST.get('peso')
        descricao = request.POST.get('descricao')

        # Converter tempo_descanso de string para timedelta
        try:
            horas, minutos, segundos = map(int, tempo_descanso_str.split(':'))
            tempo_descanso = timedelta(hours=horas, minutes=minutos, seconds=segundos)
        except ValueError:
            messages.error(request, 'Formato de tempo de descanso inválido. Use hh:mm:ss.')
            return redirect(f'/user/?treino_id={treino.id}')

        Exercicio.objects.create(
            treino=treino,
            nome=nome,
            repeticoes=repeticoes,
            tempo_descanso=tempo_descanso,
            peso=peso,
            descricao=descricao
        )
        messages.success(request, 'Exercício adicionado com sucesso!')
        return redirect(f'/user/?treino_id={treino.id}')

    return redirect('user_page')

@login_required
def remover_treino(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id, usuario=request.user)
    if request.method == 'POST':
        treino.delete()
        messages.success(request, 'Treino removido com sucesso!')
        return redirect('user_page')
    # Se chegar por GET, apenas redireciona, já que não queremos confirmar nada
    return redirect('user_page')


@login_required
def remover_exercicio(request, exercicio_id):
    exercicio = get_object_or_404(Exercicio, id=exercicio_id, treino__usuario=request.user)
    if request.method == 'POST':
        treino_id = exercicio.treino.id
        exercicio.delete()
        messages.success(request, 'Exercício removido com sucesso!')
        return redirect(f'/user/?treino_id={treino_id}')
    # Caso chegue via GET, simplesmente redireciona de volta
    return redirect('user_page')
