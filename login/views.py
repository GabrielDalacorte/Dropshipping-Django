from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib import messages


UserModel = get_user_model()


def login_user(request):
    return render(request, 'login.html')


@csrf_protect
def submit_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print('sucesso')
                    return redirect('/')
                else:
                    messages.error(request, "Sua conta nao esta confirmada!")
            else:
                messages.error(request, 'Usuário ou senha inválido. Favor tentar Novamente.')

        return redirect('/login/')


def logout_user(request):
    logout(request)
    return redirect('/login/')
