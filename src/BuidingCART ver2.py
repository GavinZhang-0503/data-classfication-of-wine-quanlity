import random
from random import randrange
import csv
import math
alldata=[]
csv_reader = csv.reader(open('D:/csc/proj/train.csv'))
for line in csv_reader:
    alldata.append(line)#read the file 读取文件

def findmax(datain,parameter):# find the biggest parameter in a certain parameter
    previous = float(datain[0][parameter])
    max=previous
    for data in range(1,len(datain)-1):
        if float(datain[data][parameter])> max:
            max = float(datain[data][parameter])
    return max

def findmin(datain,parameter):# find the smallest parameter in a certain parameter
    previous = float(datain[0][parameter])
    min=previous
    for data in range(1,len(datain)-1):
        if float(datain[data][parameter])< min:
            min = float(datain[data][parameter])
    return min

def checkentropy(data0,step,parameter):#find the best dicision for a certain parameter 定义函数 父辈数据 模拟次数 下限 上限 判断参量
    data1=data0#父辈数据
    data2=[]
    data3=[]
    bigger=0
    smaller=0
    number = 0   
    test = findmin(data0,parameter) + step# start from the smallest one
    for data in range(len(data1)-1):#for classcification
        if eval(data1[data][parameter]) >test:#父辈相应维度参数是否大于或小于边界值
            data2.append(data1[data])#如果大了，把这个数据加到data2集合# bigger data
        else:
            data3.append(data1[data])#如果小了，把这个数据加到data3集合      
    for score in range(len(data2)-1):#算第一个子类的熵# smaller data
        if eval(data2[score][11]) > 6:
            bigger += 1
        else:
            smaller +=1
    gini1 = 1- ((((bigger/len(data2))**2) +((smaller/len(data2))**2)))# calculate ginic 1
    bigger=0
    smaller=0
    for score in range(len(data3)-1):#算第二个子类
        if eval(data3[score][11]) > 6:
            bigger += 1
        else:
            smaller +=1
    gini2 = 1- ((((bigger/len(data3))**2) +((smaller/len(data3))**2)))#得到第二个熵# gini 2 
    totalgini = (gini1 + gini2)/2#子类总熵# total gini
    previousgini= totalgini
    smallestgini = totalgini# store data for a while
    output = test
    while True:
        if test < findmax(data0,parameter):# count the test numbe for all
            number += 1
        else:
            break
        test+= step
    test = findmin(data0,parameter) + step
    for time in range(number): # calculate every test
        data2=[]
        data3=[]
        bigger=0
        smaller=0
        for data in range(len(data1)-1):
            if eval(data1[data][parameter]) >test:#父辈相应维度参数是否大于或小于边界值
                data2.append(data1[data])#如果大了，把这个数据加到data2集合
            else:
                data3.append(data1[data])#如果小了，把这个数据加到data3集合
        
        for score in range(len(data2)-1):#算第一个子类的熵
            if eval(data2[score][11]) > 6:
                bigger += 1
            else:
                smaller +=1
        gini1 = 1- ((((bigger/len(data2))**2) +((smaller/len(data2))**2)))#得到第一个熵
        bigger=0
        smaller=0
        for score in range(len(data3)-1):#算第二个子类
            if eval(data3[score][11]) > 6:
                bigger += 1
            else:
                smaller +=1
        gini2 = 1- ((((bigger/len(data3))**2) +((smaller/len(data3))**2)))#得到第二个熵
        totalgini = (gini1 + gini2)/2#子类总熵
        currentgini = totalgini
        
        if currentgini < previousgini:#大小比对# find the test that minimum the gini
            output = test
            smallestgini= currentgini
            previousgini = currentgini
        test += step
    print(" ")
    print ("gini is:",smallestgini)
    return output

def qualityguess(six):# from here the tree begin
    if six > 0.85:
        second= 2.1
    else:
        second= 2.2#一级判断
    return second

lv2_1 = []
lv2_2 = []

for data in range(len(alldata)-1):
    if qualityguess(float(alldata[data][1]))==2.1:
        lv2_1.append(alldata[data])
    elif qualityguess(float(alldata[data][1]))==2.2:
        lv2_2.append(alldata[data])
count2_1 = 0
count2_2 = 0
for score in range(len(lv2_1)-1):
    if float(lv2_1[score][11]) > 6 :
        count2_1 += 1
    else:
        count2_2 += 1 

print(count2_1,"above 6")
print(count2_2,"below 6")
print ("the length of lv2_2",len(lv2_2))

def qualityguess2(six):
    if six > 9.19:
        second= 2.1
    else:
        second= 2.2#一级判断
    return second

lv3_1 = []
lv3_2 = []

for data in range(len(lv2_2)-1):
    if qualityguess2(float(lv2_2[data][10]))==2.1:
        lv3_1.append(lv2_2[data])
    elif qualityguess2(float(lv2_2[data][10]))==2.2:
        lv3_2.append(lv2_2[data])
count3_1 = 0
count3_2 = 0
for score in range(len(lv3_2)-1):
    if float(lv3_2[score][11]) > 6 :
        count3_1 += 1
    else:
        count3_2 += 1 

print(count3_1,"above 6")
print(count3_2,"below 6")
print ("the length ",len(lv3_2))

#print("for the parameter",9,",the output is",checkentropy(lv2_2,0.01,9))

def qualityguess3(six):
    if six > 9.49:
        second= 2.1
    else:
        second= 2.2#一级判断
    return second

lv4_1 = []
lv4_2 = []

for data in range(len(lv3_1)-1):
    if qualityguess3(float(lv3_1[data][10]))==2.1:
        lv4_1.append(lv3_1[data])
    elif qualityguess3(float(lv3_1[data][10]))==2.2:
        lv4_2.append(lv3_1[data])
count4_1 = 0
count4_2 = 0
for score in range(len(lv4_1)-1):
    if float(lv4_1[score][11]) > 6 :
        count4_1 += 1
    else:
        count4_2 += 1 

print(count4_1,"above 6")
print(count4_2,"below 6")
print ("the length ",len(lv4_1))

def qualityguess4(six):
    if six > 0.54:
        second= 2.1
    else:
        second= 2.2#一级判断
    return second

lv5_1 = []
lv5_2 = []

for data in range(len(lv4_1)-1):
    if qualityguess4(float(lv4_1[data][9]))==2.1:
        lv5_1.append(lv4_1[data])
    elif qualityguess4(float(lv4_1[data][9]))==2.2:
        lv5_2.append(lv4_1[data])
count5_1 = 0
count5_2 = 0
for score in range(len(lv5_2)-1):
    if float(lv5_2[score][11]) > 6 :
        count5_1 += 1
    else:
        count5_2 += 1 

print(count5_1,"above 6")
print(count5_2,"below 6")
print ("the length ",len(lv5_2))

def qualityguess5(six):
    if six > 106:
        second= 2.1
    else:
        second= 2.2#一级判断
    return second

lv6_1 = []
lv6_2 = []

for data in range(len(lv5_1)-1):
    if qualityguess5(float(lv5_1[data][6]))==2.1:
        lv6_1.append(lv5_1[data])
    elif qualityguess5(float(lv5_1[data][6]))==2.2:
        lv6_2.append(lv5_1[data])
count6_1 = 0
count6_2 = 0
for score in range(len(lv6_1)-1):
    if float(lv6_1[score][11]) > 6 :
        count6_1 += 1
    else:
        count6_2 += 1 

print(count6_1,"above 6")
print(count6_2,"below 6")
print ("the length ",len(lv6_1))

def qualityguess6(six):
    if six > 0.6:
        second= 2.1
    else:
        second= 2.2#一级判断
    return second

lv7_1 = []
lv7_2 = []

for data in range(len(lv6_2)-1):
    if qualityguess6(float(lv6_2[data][1]))==2.1:
        lv7_1.append(lv6_2[data])
    elif qualityguess6(float(lv6_2[data][1]))==2.2:
        lv7_2.append(lv6_2[data])
count7_1 = 0
count7_2 = 0
for score in range(len(lv7_1)-1):
    if float(lv7_1[score][11]) > 6 :
        count7_1 += 1
    else:
        count7_2 += 1 

print(count7_1,"above 6")
print(count7_2,"below 6")
print ("the length ",len(lv7_1))

def qualityguess7(six):
    if six > 0.109:
        second= 2.1
    else:
        second= 2.2#一级判断
    return second

lv8_1 = []
lv8_2 = []

for data in range(len(lv7_2)-1):
    if qualityguess7(float(lv7_2[data][4]))==2.1:
        lv8_1.append(lv7_2[data])
    elif qualityguess7(float(lv7_2[data][4]))==2.2:
        lv8_2.append(lv7_2[data])
count8_1 = 0
count8_2 = 0
for score in range(len(lv8_2)-1):
    if float(lv8_2[score][11]) > 6 :
        count8_1 += 1
    else:
        count8_2 += 1 

print(count8_1,"above 6")
print(count8_2,"below 6")
print ("the length ",len(lv8_2))

def qualityguess8(six):
    if six > 9.7:
        second= 2.1
    else:
        second= 2.2#一级判断
    return second

lv9_1 = []
lv9_2 = []

for data in range(len(lv8_2)-1):
    if qualityguess8(float(lv8_2[data][10]))==2.1:
        lv9_1.append(lv8_2[data])
    elif qualityguess8(float(lv8_2[data][10]))==2.2:
        lv9_2.append(lv8_2[data])
count9_1 = 0
count9_2 = 0
for score in range(len(lv9_2)-1):
    if float(lv9_2[score][11]) > 6 :
        count9_1 += 1
    else:
        count9_2 += 1 

print(count9_1,"above 6")
print(count9_2,"below 6")
print ("the length ",len(lv9_2))

def qualityguess9(six):
    if six > 56:
        second= 2.1
    else:
        second= 2.2#一级判断
    return second

lv10_1 = []
lv10_2 = []

for data in range(len(lv9_1)-1):
    if qualityguess9(float(lv9_1[data][6]))==2.1:
        lv10_1.append(lv9_1[data])
    elif qualityguess9(float(lv9_1[data][6]))==2.2:
        lv10_2.append(lv9_1[data])
count10_1 = 0
count10_2 = 0
for score in range(len(lv10_1)-1):
    if float(lv10_1[score][11]) > 6 :
        count10_1 += 1
    else:
        count10_2 += 1 

print(count10_1,"above 6")
print(count10_2,"below 6")
print ("the length ",len(lv10_1))

def qualityguess10(six):
    if six > 0.59:
        second= 2.1
    else:
        second= 2.2#一级判断
    return second

lv11_1 = []
lv11_2 = []

for data in range(len(lv10_2)-1):
    if qualityguess10(float(lv10_2[data][1]))==2.1:
        lv11_1.append(lv10_2[data])
    elif qualityguess10(float(lv10_2[data][1]))==2.2:
        lv11_2.append(lv10_2[data])
count11_1 = 0
count11_2 = 0
for score in range(len(lv11_1)-1):
    if float(lv11_1[score][11]) > 6 :
        count11_1 += 1
    else:
        count11_2 += 1 

print(count11_1,"above 6")
print(count11_2,"below 6")
print ("the length ",len(lv11_1))

def qualityguess11(six):
    if six > 3.449:
        second= 2.1
    else:
        second= 2.2#一级判断
    return second

lv12_1 = []
lv12_2 = []

for data in range(len(lv11_2)-1):
    if qualityguess11(float(lv11_2[data][8]))==2.1:
        lv12_1.append(lv11_2[data])
    elif qualityguess11(float(lv11_2[data][8]))==2.2:
        lv12_2.append(lv11_2[data])
count12_1 = 0
count12_2 = 0
for score in range(len(lv12_1)-1):
    if float(lv12_1[score][11]) > 6 :
        count12_1 += 1
    else:
        count12_2 += 1 

print(count12_1,"above 6")
print(count12_2,"below 6")
print ("the length ",len(lv12_1))

def qualityguess12(six):
    if six > 0.9976:
        second= 2.1
    else:
        second= 2.2#一级判断
    return second

lv13_1 = []
lv13_2 = []

for data in range(len(lv12_2)-1):
    if qualityguess12(float(lv12_2[data][7]))==2.1:
        lv13_1.append(lv12_2[data])
    elif qualityguess12(float(lv12_2[data][7]))==2.2:
        lv13_2.append(lv12_2[data])
count13_1 = 0
count13_2 = 0
for score in range(len(lv13_1)-1):
    if float(lv13_1[score][11]) > 6 :
        count13_1 += 1
    else:
        count13_2 += 1 

print(count13_1,"above 6")
print(count13_2,"below 6")
print ("the length ",len(lv13_1))

print("the output for",0,"is",checkentropy(lv12_2,0.1,0))
print("the output for",1,"is",checkentropy(lv12_2,0.01,1))
print("the output for",2,"is",checkentropy(lv12_2,0.01,2))
print("the output for",3,"is",checkentropy(lv12_2,0.1,3))
print("the output for",4,"is",checkentropy(lv12_2,0.001,4))
print("the output for",5,"is",checkentropy(lv12_2,1,5))
print("the output for",6,"is",checkentropy(lv12_2,1,6))
print("the output for",7,"is",checkentropy(lv12_2,0.00001,7))
print("the output for",8,"is",checkentropy(lv12_2,0.01,8))
print("the output for",9,"is",checkentropy(lv12_2,0.01,9))
print("the output for",10,"is",checkentropy(lv12_2,0.1,10))