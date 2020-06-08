import random
from random import randrange
import csv
import math
alldata=[]
csv_reader = csv.reader(open('D:/csc/proj/test.csv'))
for line in csv_reader:
    alldata.append(line)#open the file

lv4_1 = []
lv4_2 = []
goodwine = []
badwine = []

def guess1to3(data):#this part use if to conduct the Classfication Tree.
    global lv4_1
    global lv4_2
    if eval(data[1]) <= 0.85:
        if eval(data[10]) > 9.19:
            if eval(data[10]) > 9.49:
                if eval(data[9]) >0.54:
                    if eval(data[6]) <= 106:
                        if eval(data[1])<= 0.6:
                            if eval(data[4]) <= 0.109:
                                if eval(data[10])>9.7:
                                    if eval(data[6])<=56:
                                        if eval(data[1]) <= 0.59:
                                            if eval(data[8]) <= 3.449:
                                                if eval(data[7]) <= 0.9976:
                                                    if4_1 = 1
                                                    data.append(7)#guess it is a good wine
                                                else:
                                                    if4_1 = 3
                                                    data.append(5)#guess it is a bad wine
                                            else:
                                                if4_1 = 3
                                                data.append(5)#guess it is a bad wine
                                        else:
                                            if4_1 = 3
                                            data.append(5)#guess it is a bad wine
                                    else:
                                        if4_1 = 3
                                        data.append(5)#guess it is a bad wine
                                else:
                                    if4_1 = 3
                                    data.append(5)#guess it is a bad wine
                            else:
                                if4_1 = 3
                                data.append(5)#guess it is a bad wine
                        else:
                            data.append(5)#guess it is a bad wine
                            if4_1 = 3
                    else:
                        data.append(5)#guess it is a bad wine
                        if4_1 = 3
                else:
                    data.append(5)#guess it is a bad wine
                    if4_1 = 3
            else:
                data.append(5)#guess it is a bad wine
                if4_1 = 3
        else:
            data.append(5)#guess it is a bad wine
            if4_1 = 3
    else:
        data.append(5)#guess it is a bad wine
        if4_1 = 3
    return if4_1

for data in range(len(alldata)-1):
    if guess1to3(alldata[data]) == 1:#load the dataset and judge data one by one
        goodwine.append(alldata[data])# store the prediction result
    else:
        badwine.append(alldata[data])

countRight = 0
countFalse = 0

for wine in goodwine:#calculate the accuracy
    if eval(wine[11]) <= 6:
        wine[11] = 5
    else:
        wine[11] = 7
    
    if wine[11] == wine[12]:
        countRight += 1
    else:
        countFalse +=1

for data in badwine:
    if eval(data[11]) <= 6:
        data[11] = 5
    else:
        data[11] = 7
    
    if data[11] == data[12]:
        countRight += 1
    else:
        countFalse +=1

#preval(countRight, countRight)
accuracy = countRight/len(alldata)
#preval(accuracy)
print("predict complete,the accuracy is",accuracy)
