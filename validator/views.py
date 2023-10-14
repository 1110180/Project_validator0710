from django.shortcuts import render
from .forms import *
# Create your views here.


def index(req):
    return render(req, 'index.html')


def formcomment(req):
    nashaforma = UserComment()
    data = {'form': nashaforma}
    print(1)
    if req.POST:
        nashaforma = UserComment(req.POST)
        data = {'form': nashaforma}
        print(2)
        if nashaforma.is_valid():
            print(3)
            k1 = nashaforma.cleaned_data.get('name')
            k2 = nashaforma.cleaned_data.get('comment')
            # k1 = req.POST.get('name')
            data = {'name': k1, 'com': k2}
            return render(req, 'finish.html', data)
    return render(req, 'forma.html', data)


def finish(req):
    data = {}
    return render(req, 'finish.html', data)


def formtel(req):
    nashaforma = UserTel()
    data = {'form234': nashaforma}
    if req.POST:
        nashaforma = UserTel(req.POST)
        data = {'form234': nashaforma}
        if nashaforma.is_valid():
            print(3)
            k1 = nashaforma.cleaned_data.get('name')
            k2 = nashaforma.cleaned_data.get('tel')
            k3 = nashaforma.cleaned_data.get('tarif')
            # k1 = req.POST.get('name')
            data = {'name': k1, 'tel': k2, 'tarif': k3}
            return render(req, 'finish.html', data)
    return render(req, 'forma.html', data)


