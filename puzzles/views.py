from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import GraderForm
from hashlib import md5
from .models import Puzzle, Submission
from users.models import Team
from datetime import datetime

def findCurrentPuzzle(request):
    currentTeam = Team.objects.get(username=request.session['username'])
    
    currentPuzzle = 1
    if(Submission.objects.filter(team=currentTeam,result=True)):
        correct = Submission.objects.filter(team=currentTeam,result=True)
        currentPuzzle = max(correct,key=lambda x: x.puzzle.number).puzzle.number+1

    return currentPuzzle

# Create your views here.
def submit(request):
    if(request.session['username']==''):
        return HttpResponseRedirect(reverse('users:login'))
    else:
        form = GraderForm(request)
        currentTeam = Team.objects.get(username=request.session['username'])
        numIncorrect = len(Submission.objects.filter(team=currentTeam))-(findCurrentPuzzle(request)-1)
        return render(request,'puzzles/submit.html',{'form':form,'numIncorrect':numIncorrect})

def grade(request):
    currentTeam = Team.objects.get(username=request.session['username'])
    
    currentPuzzle = findCurrentPuzzle(request)
    
    m = md5()
    m.update(request.POST['answer'].lower().encode())
    hashed = m.hexdigest()

    s = Submission(team=currentTeam,puzzle=Puzzle.objects.get(number=currentPuzzle),time=datetime.now(),submitAnswer=hashed)
    if(Puzzle.objects.filter(number=currentPuzzle,answer=hashed)):
        s.result=True

    s.save()
    return HttpResponseRedirect(reverse('puzzles:submit'))

def scoreboard(request):
    t = Team.objects.all()
    teamList = []
    for i in t:
        q = {'Name':i.team_name}
        currentPuzzle = 1
        if(Submission.objects.filter(team=i,result=True)):
            correct = Submission.objects.filter(team=i,result=True)
            currentPuzzle = max(correct,key=lambda x: x.puzzle.number).puzzle.number+1
        q['Puzzle']=currentPuzzle
        teamList.append(q)

    teamList = sorted(teamList,key=lambda x: x['Puzzle'],reverse=True)
    return render(request,'puzzles/grader.html',{'teamList':teamList})
