from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from finance.models import Transaction, Goal

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title','amount','transaction_type','date','category']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name','target_amount','deadline']