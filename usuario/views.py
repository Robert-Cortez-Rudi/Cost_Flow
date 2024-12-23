from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import UserSignForm, UserLoginForm, EditProfileForm

def home(request):
    return render(request, 'home.html')

# View Login
@require_http_methods(['GET', 'POST'])
def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Usuário ou senha inválida!")
                return redirect("login")
    else:
        form = UserLoginForm()
    return render(request, "login.html", {"form": form})


# View Register
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserSignForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User

@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == "POST":
        form = UserSignForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]

            if User.objects.filter(username=username).exists():
                messages.error(request, "Nome de usuário já existe. Por favor, escolha outro.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email já registrado. Por favor, use outro email.")
            elif password != confirm_password:
                messages.error(request, "As senhas não coincidem. Por favor, tente novamente.")
            else:
                try:
                    user = User(
                        username=username,
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    user.set_password(password)
                    user.save()

                    user = authenticate(
                        request,
                        username=username,
                        password=password
                    )

                    if user is not None:
                        login(request, user)                        
                        return redirect("home")
                    else:
                        messages.error(request, "Erro na autenticação do usuário.")
                except Exception as e:
                    messages.error(request, f"Erro ao criar o usuário: {e}")
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = UserSignForm()
    return render(request, "register.html", {"form": form})


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect("home")

@login_required(login_url="login")
def profile(request):
    user = request.user
    context = {
        "user": user
    }
    return render(request, "profile.html", context)

@login_required(login_url="login")
@require_http_methods(['GET', 'POST'])
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect("home")
    else:
        form = EditProfileForm(instance=user)
    return render(request, "edit_profile.html", {"form": form})

@login_required(login_url="login")
def delete_profile(request):
    user = request.user
    user.delete()
    messages.success(request, "Conta deletada com sucesso!")
    return redirect("home")