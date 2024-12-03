from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def register(request):
    # Registration logic
    return render(request, 'register.html')

def user_page(request):
    # User page logic
    return render(request, 'user.html')