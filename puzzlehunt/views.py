from django.shortcuts import render

def home(request):
    return render(request,'puzzlehunt/index.html')

def about(request):
    return render(request,'puzzlehunt/about.html')
