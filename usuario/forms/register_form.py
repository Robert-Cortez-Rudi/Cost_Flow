from django import forms
from ..models import User

class UserSignForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder": "Usuário", "class": "form-control"}),
                               label="Usuário")
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder": "Nome", "class": "form-control"}),
                                label="Nome")
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder": "Sobrenome", "class": "form-control"}),
                                label="Sobrenome")
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}), 
                                label="Email")
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={"placeholder": "Senha", "class": "form-control"}), 
                               label="Senha", strip=False)
    confirm_password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={"placeholder": "Confirmar Senha", "class": "form-control"}), 
                                       label="Confirmar Senha", strip=False)
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password", "confirm_password"]


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email já cadastrado!")
        return email
    

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("As senhas não conferem!")
        return cleaned_data
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    
