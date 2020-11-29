from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from accounts.models import OthersInfo

# Accounts forms.py file

class CreateUserForm(UserCreationForm):
    class Meta():
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].label = 'Nome'
        self.fields['first_name'].required = True

        self.fields['last_name'].label = 'Apelido'
        self.fields['last_name'].required = True

        self.fields['username'].label = 'Digite o seu nome de usuário'

        self.fields['email'].label = 'Endereço de E-mail'

        self.fields['password1'].label = 'Palavra-passe'

        self.fields['password2'].label = 'Confirmação da Palavra-passe'

class OthersInfoForm(forms.ModelForm):
    class Meta():
        fields = ['sexo', 'bio', 'image']
        model = OthersInfo
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = 'Foto de perfil'
        self.fields['bio'].label = 'Fale um pouco de ti'

field_bio = OthersInfoForm.base_fields['bio']
field_bio.widget.attrs['rows'] = 4