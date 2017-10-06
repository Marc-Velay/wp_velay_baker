from django.shortcuts import render
import csv
from django.conf import settings

# Create your views here.

def index(request):
    '''
    Default function when loading the page: send back a rendered version of index.html
    '''
    context = {}
    loadFromCSV()
    return render(request, 'gatherer/index.html', context)

def loadFromCSV():
    print("Hello")
    with open('media/gatherer/DAT_MT_EURUSD_M1_201709.csv', 'rt') as f:
        reader = csv.reader(f, delimiter = ",")
        for line in reader:
            print (line)


def test(request):
    '''
    Default function when loading the page: send back a rendered version of index.html
    '''
    context = {}
    loadFromCSV()
    return render(request, 'gatherer/index.html', context)
