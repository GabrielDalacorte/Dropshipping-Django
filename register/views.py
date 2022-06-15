from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from register.forms import RegisterForm

UserModel = get_user_model()


def register(request):
    if request.user.is_authenticated:
       return redirect('/')
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
        #user.is_active = True
        user.save()
        messages.success(request, "Sua conta está ativada agora, você pode fazer o login")
        return redirect('/')
    else:
        messages.warning(request, "Link de ativação é inválido")
        return redirect('register')


def activate_endpoint(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if User is not None and default_token_generator.check_token(user, token):
        user.save()
        responseData = {"Sucesso": "Sua conta está ativa!"}
        return JsonResponse(responseData)
    else:
        responseData = {"Erro": "Link inválido"}
        return JsonResponse(responseData)