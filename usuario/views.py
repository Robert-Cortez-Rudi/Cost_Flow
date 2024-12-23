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
def login(request):
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
@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == "POST":
        form = UserSignForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            login(request, user)
            messages.success(request, f"Usuário {username} criado com sucesso!")
            return redirect("home")    
    else:
        form = UserSignForm()
    return render(request, "register.html", {"form": form})


@login_required(login_url="login")
def logout(request):
    logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect("home")

@login_required(login_url="login")
def profile(request):
    return render(request, "profile.html")

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
