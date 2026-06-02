from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AccountForm(forms.ModelForm):
    '''Форма для создания (редактирования) учетной записи '''
    class Meta:
        # Модель, которую мы используем для создания формы
        model = Account
        # Поля, которые будут отображаться в форме
        fields = ('site','login','password')
        
# Форма для регистрации пользователя
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)