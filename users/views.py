from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import LoginForm, RegisterForm
from hashlib import md5
from .models import Team

def logout(request):
    request.session['username'] = ''
    return HttpResponseRedirect(reverse('users:index'))
    
def login(request):
    username = request.session.get('username','')
    if(username!=''):
        return HttpResponseRedirect(reverse('users:index'))
    else:
        form = LoginForm()
        return render(request,'users/login.html',{'form':form})

def submit(request):
    username = request.POST['username']
    password = request.POST['password']

    m = md5()
    m.update(password.encode())
    hashedPassword = m.hexdigest()

    matches = Team.objects.filter(username=username,password=hashedPassword)
    if(len(matches)==1):
        request.session['username'] = username
        return HttpResponseRedirect(reverse("users:index"))
    else:
        return HttpResponseRedirect(reverse("users:login"))

def home(request):
    return HttpResponse("Home View")

def index(request):
    username = request.session.get('username','')
    teamName = ''
    if(username!=''):
        teamName = Team.objects.get(username=username).team_name
    context = {'teamName':teamName}
    template = loader.get_template("users/index.html")
    response = HttpResponse(template.render(context,request))
    return response

def register(request):
    username = request.session.get('username','')
    if(username!=''):
        return HttpResponseRedirect(reverse('users:index'))
    else:
        form = RegisterForm()
        return render(request,'users/register.html',{'form':form})
def create(request):
    username = request.POST['username']
    password = request.POST['password']
    confirmPassword = request.POST['confirmPassword']
    teamName = request.POST['teamName']

    if(len(Team.objects.filter(username=username))!=0 or password!=confirmPassword or len(Team.objects.filter(team_name=teamName))!=0):
        return HttpResponseRedirect(reverse('users:register'))
    else:
        m = md5()
        m.update(password.encode())
        hashedPassword = m.hexdigest()
        t = Team(username=username,password=hashedPassword,team_name=teamName)
        t.save()
        request.session['username'] = username
        return HttpResponseRedirect(reverse('users:index'))


    


