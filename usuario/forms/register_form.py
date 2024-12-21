from django import forms
from models import User

class UserSignForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Senha", "class": "form-control"}), 
                               label="Senha", strip=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirmar Senha", "class": "form-control"}), 
                                       label="Confirmar Senha", strip=False)
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password", "confirm_password"]

    def __init__(self, *args, **kyargs):
        super().__init__(*args, **kyargs)
        self.fields["username"].widget.attrs["autofocus"] = True
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Usuário"

        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["placeholder"] = "Email"

        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["placeholder"] = "Primeiro Nome"

        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["placeholder"] = "Sobrenome"


    def clean_email(self):
        email = self.cleaned_data().get("email")
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
    
