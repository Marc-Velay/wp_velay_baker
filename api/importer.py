from django.shortcuts import render
import csv
from django.conf import settings
from datetime import datetime
from api.models import *

def createDateTime(date,time):
        DateAndTime = date + " " + time
        dt = datetime.strptime(DateAndTime, '%Y.%m.%d %H:%M')
        return dt

def loadFromCSV():
    print("Hello")
    i=1
    with open('media/gatherer/DAT_MT_EURUSD_M1_201709.csv', 'rt') as f:
        reader = csv.reader(f, delimiter = ",")
        for row in reader:
            DateAndTime = createDateTime(row[0],row[1])
            _, created = Forex.objects.get_or_create(
                timestamp = DateAndTime,
                opening = row[2],
                high = row[3],
                low = row[4],
                closing = row[5],
                )
            print("Created row : "+ str(i) + "")
            i=i+1
    print("Done")
