from django.shortcuts import render
import csv
from django.conf import settings
from datetime import datetime
from gatherer.models import Item

# Create your views here.

def index(request):
    '''
    Default function when loading the page: send back a rendered version of index.html
    '''
    context = {}
    loadFromCSV()
    return render(request, 'gatherer/index.html', context)

#Function to format date and time correctly
def createDateTime(date,time):
    DateAndTime = date + " " + time
    dt = datetime.strptime(DateAndTime, '%Y.%m.%d %H:%M')
    return dt

#CSV loader function
def loadFromCSV():
    with open('media/gatherer/DAT_MT_EURUSD_M1_201709.csv', 'rt') as f:
        reader = csv.reader(f, delimiter = ",")
        for row in reader:
            DateAndTime = createDateTime(row[0],row[1])
            _, created = Item.objects.get_or_create(
                name = "Forex",
                source = "HistData.com",
                timestamp = DateAndTime,
                opening = row[2],
                high = row[3],
                low = row[4],
                closing = row[5],
                )

def test(request):
    '''
    Default function when loading the page: send back a rendered version of index.html
    '''
    context = {}
    loadFromCSV()
    return render(request, 'gatherer/index.html', context)
