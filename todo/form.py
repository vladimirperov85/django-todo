from django import forms
from .models import Account, Todo
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
        
class TodoForm(forms.ModelForm):
    '''Форма для создания дела'''
    class Meta:
        model = Todo
        fields = ('title', 'note')
        widgets = {
            'title': forms.TextInput(attrs={'size': 50}),  # ← Увеличили ширину
            'note': forms.Textarea(attrs={'rows': 4, 'cols': 50}),  # ← Текстовая область
        }