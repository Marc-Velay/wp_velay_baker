from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    Default function when loading the page: send back a rendered version of index.html
    '''
    context = {}
    loadFromCSV()
    return render(request, 'gatherer/index.html', context)

def loadFromCSV():
    print("nothing loaded :D")
    print("TODO load CSV from webpage and parse")


def test(request):
    '''
    Default function when loading the page: send back a rendered version of index.html
    '''
    context = {}
    print("testing")
    return render(request, 'gatherer/index.html', context)
