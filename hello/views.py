from django.shortcuts import render, redirect

from hello import models


# Create your views here.

def helloWorld(request):
    return render(request, 'main.html')


def create(request):
    text = request.POST['text']
    models.Something.objects.create(text=text)
    return redirect('/show/')
    # return show(request)


def show(request):
    query = models.Something.objects.all()
    texts = []
    for idx, p in enumerate(query):
        texts.append({'id': idx, 'text': p.text})
    return render(request, 'list.html', {'texts': texts})
