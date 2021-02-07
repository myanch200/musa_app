from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Poem
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        

class CreatePoemForm(ModelForm):
    class Meta:
        model = Poem
        fields = '__all__'
        exclude = ['author']