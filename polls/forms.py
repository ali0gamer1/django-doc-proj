from django import forms
from .models import Question
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PollCreateForm(forms.ModelForm):

    votes_string = forms.CharField(max_length = 200,label = "votes (separated by commas)")
    
    class Meta:
        model = Question
        fields = ["question_text", "votes_string", "users", "single_choice"]
        exclude = ["users"]


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
    

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    