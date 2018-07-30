from django import forms
from .models import *
from users.models import *

class GraderForm(forms.Form):
    def __init__(self,request,*args,**kwargs):
        super (GraderForm,self).__init__(*args,**kwargs)

        currentTeam = Team.objects.get(username=request.session['username'])

        if(not Submission.objects.filter(team=currentTeam,result=True)):
            self.currentPuzzle = 1
        else:
            correct = Submission.objects.filter(team=currentTeam,result=True)
            self.currentPuzzle = max(correct,key=lambda x: x.puzzle.number).puzzle.number+1

        self.fields['answer']=forms.CharField(label='Puzzle '+str(self.currentPuzzle)+': ',max_length=200)
