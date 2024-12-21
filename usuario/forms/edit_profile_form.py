from django import forms
from models import User

class EditProfileForm(forms.ModelForm):
    # Não editáveis

    email = forms.EmailField(disabled=True, widget=forms.EmailInput(attrs={"class": "form-control",
                                                                           "style": "#e9ecef;"}))
    password = forms.PasswordInput(disabled=True, widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                                   "style": "#e9ecef;"}))
    
    # Editáveis

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "style": "#FFF;"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "style": "#FFF;"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "style": "#FFF;"}))
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Usuário"
        self.fields["first_name"].widget.attrs["placeholder"] = "Primeiro Nome"
        self.fields["last_name"].widget.attrs["placeholder"] = "Sobrenome"
