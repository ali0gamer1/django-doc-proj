from django.shortcuts import render,HttpResponse, redirect

from .models import *
from .forms import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

@login_required(login_url = "/login")
def index(request):
    
    return render(request, "index.html", {"polls" : Question.objects.all()})

def logout_view(request):

    logout(request)

    return redirect("/")

def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")

    else:
        form = SignUpForm()
    
    return render(request, "sign_up.html", {"form" : form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)

                return redirect("/")
        
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form" : form})
        

@login_required(login_url = "/login")
def vote_view(request, hes):

    return render(request, "vote.html", {"poll":Question.objects.get(id = hes)})

@login_required(login_url = "/login")
def vote_choice_view(request, hes, choice):

    q = Question.objects.get(id = hes)
    
    if q.single_choice:
        for c in q.choice.all():
            if request.user in c.users.all():
                    c.votes -= 1
                    c.users.remove(request.user)
                    c.save()
                       
    c = q.choice.get(id = choice)
    
    if request.user not in c.users.all():
        c.votes += 1
        c.users.add(request.user)
        c.save()
    else:
        c.votes -= 1
        c.users.remove(request.user)
        c.save()

    return redirect(f"../")

@login_required(login_url = "/login")
def create(request):
    
    if request.method == "POST":
        form = PollCreateForm(request.POST)
        
        if form.is_valid():
        
            poll = form.save()
            
            votes = form.cleaned_data["votes_string"]
            votes = votes.split(",")
            for v in votes:
                c = Choice(choice_text = v)
                c.save()
                poll.choice.add(c)
            poll.save()

            
            return redirect("/")

    else:
        form = PollCreateForm()
    
    return render(request, "create.html", {"form" : form})
