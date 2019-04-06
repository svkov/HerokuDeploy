from django.shortcuts import render, redirect

from hello import models


# Create your views here.

def helloWorld(request):
    return render(request, 'main.html')


def create(request):
    if request.method == 'POST':
        try:
            text = request.POST['text']
        except:
            print('smth went wrong')
            print(request.POST)
            print(request.method)
            return redirect('/')
        models.Something.objects.create(text=text).save()
        return redirect('/show/')
    # return redirect('/')


def show(request):
    query = models.Something.objects.all()
    texts = []
    for idx, p in enumerate(query):
        texts.append({'id': idx, 'text': p.text})
    return render(request, 'list.html', {'texts': texts})
