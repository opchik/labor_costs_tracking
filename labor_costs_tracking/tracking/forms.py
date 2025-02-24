from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Project, WorkLog, User, Client, Department, Task


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].empty_label = None

    client = forms.ModelChoiceField(label='Клиент', queryset=Client.objects.all(), widget=forms.Select(attrs={'class': 'form-input'}))
    name = forms.CharField(label='Название проекта', widget=forms.TextInput(attrs={'class': 'form-input'}))
    amount = forms.DecimalField(label='Сумма', max_digits=10, decimal_places=0, widget=forms.NumberInput(attrs={'class': 'form-input'}))
    start_date = forms.DateField(label='Дата начала', widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}))
    end_date = forms.DateField(label='Дата окончания', widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}))
    class Meta:
        model = Project
        fields = ['client', 'name', 'amount', 'start_date', 'end_date']


class WorkLogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].empty_label = None
        self.fields['department'].empty_label = None
        self.fields['task'].empty_label = None

    project = forms.ModelChoiceField(label='Проект', queryset=Project.objects.all(), widget=forms.Select(attrs={'class': 'form-input'}))
    date = forms.DateField(label='Дата', widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}))
    department = forms.ModelChoiceField(label='Отдел', queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'form-input'}))
    task = forms.ModelChoiceField(label='Задача', queryset=Task.objects.all(), widget=forms.Select(attrs={'class': 'form-input'}))
    hours_spent = forms.DecimalField(label='Часы', max_digits=5, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-input'}))
    class Meta:
        model = WorkLog
        fields = ['project', 'date', 'department', 'task', 'hours_spent']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'profile-form'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'profile-form'}))

    class Meta:
        model = User
        fields = ('username', 'email')


class AdditionalCostsForm(forms.ModelForm):
    additional_costs = forms.DecimalField(label='Прямые расходы', max_digits=10, decimal_places=0, widget=forms.NumberInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Project
        fields = ['additional_costs']
