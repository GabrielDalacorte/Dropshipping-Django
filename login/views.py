from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib import messages
from login.forms import RegisterForm


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


def register(request):
    if request.user.is_authenticated:
       return redirect('index')
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.is_active = False

                current_site = get_current_site(request)
                mail_subject = 'Ative sua conta'
                message = render_to_string('account.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                send_mail = form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message, to=[send_mail])
                email.send()
                messages.success(request, 'Conta criada com sucesso')
                messages.info(request, 'Ative sua conta a partir do e-mail que você forneceu')
                return redirect('/')
            else:
                messages.error(request, 'Usuário ou senha inválido. Favor tentar Novamente.')
        else:
            form = RegisterForm()
        context = {"form": form}
        return render(request, "register.html", context)


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if User is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Sua conta está ativada agora, você pode fazer o login")
        return redirect('/')
    else:
        messages.warning(request, "Link de ativação é inválido")
        return redirect('register')


def logout_user(request):
    logout(request)
    return redirect('/login/')
