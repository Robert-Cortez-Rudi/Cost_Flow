from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
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
                messages.success(request, f"Login efetuado com sucesso!")
                return redirect("home")
            else:
                messages.error(request, "Usuário ou senha inválida!")
    else:
        form = UserLoginForm()
    return render(request, "login.html", {"form": form})


# View Register
@require_http_methods(['GET', 'POST'])
def register(request):
    pass # Finalizar