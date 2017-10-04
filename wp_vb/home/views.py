from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    Default function when loading the page: send back a rendered version of index.html
    '''
    context = {}
    return render(request, 'home/index.html', context)

def test(request):
    '''
    Default function when loading the page: send back a rendered version of index.html
    '''
    context = {}
    return render(request, 'home/test.html', context)

