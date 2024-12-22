from django import forms
from ..models import User

class EditProfileForm(forms.ModelForm):
    # Não editável

    email = forms.EmailField(disabled=True, widget=forms.EmailInput(attrs={"class": "form-control",
                                                                           "style": "#e9ecef;"}))    
    # Editáveis

    username = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", "style": "#FFF;"}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", "style": "#FFF;"}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", "style": "#FFF;"}))
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Usuário"
        self.fields["first_name"].widget.attrs["placeholder"] = "Primeiro Nome"
        self.fields["last_name"].widget.attrs["placeholder"] = "Sobrenome"

        if self.instance:
            self.fields["username"].initial = self.instance.username
            self.fields["first_name"].initial = self.instance.first_name
            self.fields["last_name"].initial = self.instance.last_name

