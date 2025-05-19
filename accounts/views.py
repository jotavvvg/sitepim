from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.first_name = first_name
            user.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('login')
    return render(request, 'accounts/signup.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:niveis')  
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'accounts/login.html')

