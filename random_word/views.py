from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    request.session['random']=0
    return render(request, 'index.html')


def randomWord(request):
    if 'random' not in request.session:
        request.session['random']=0
    request.session['random']+=1    
    context = {
        'random' : get_random_string(length=14),
    }
    return render(request, 'index.html', context)


def reset(request):
    request.session['random']=0
    return redirect('/random_word')


