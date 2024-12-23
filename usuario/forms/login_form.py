from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label="Usuário",
        widget=forms.TextInput(attrs={"placeholder": "Usuário", "class": "form-control"})
    )
    password = forms.CharField(
        max_length=128,
        label="Senha",
        widget=forms.PasswordInput(attrs={"placeholder": "Senha", "class": "form-control"})
    )