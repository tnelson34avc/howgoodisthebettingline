# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:32:38 2022

@author: nelso

Title: how good is the batting linee (hw)
Status: completed
"""

"""
attached is a file of the first 8 weeks of the NFL season.  Columns are week, visit team, home team, the line (first entry is DAL at TB the betting line is -7.5, that means bookmakers expect if a large number of games were played between DAL and TB, at TB, the average difference in scores would be Tampa Bay to win by 7.5.  The last column is the actual difference; in this case TB actually won by 2.   

Line 12  CLE at KC- the betting line is -8.  That means that the bookmakers expect, on average, KC would win by 8   The average difference in score CLE - KC would be 8.  So the betting line is KC-8.  And it turned out that KC LOST the game by 4.

Using the data in the .csv file, construct a linear model:  actual score = b0 + b1* line

If the bookmakers were perfect, b0 would be 0 and b1 would be 1.             lineVSactual.csv 

Interpret the results.  Is b0 significantly different from 0?    Is b1 significantly different from 1?

What does this mean about betting line in the NFL?
"""
import pandas as pd
from os import chdir
import matplotlib.pyplot as plt
import numpy as np

chdir('D:/cs177/hw_txt_doc')# you can use \\ or / for file location


#D:/cs177/hw_txt_doc/
dataset = pd.read_csv('lineVSactual-1.csv')#dataset = pd.read_csv('lineVSactual-1')

type(dataset)
dataset.columns
bl = dataset['line']
result = dataset['actual']

plt.hist(dataset['line'], alpha = 0.5, label = 'line', density = True)
plt.hist(dataset['actual'], alpha = 0.5, label = 'actual', density = True)
plt.legend()
plt.grid()
plt.show() #
# dataset.hist('line')
# dataset.hist('actual', alpha = 0.5)

print(f"the mean of the line: {np.mean(bl): .2f}")
print(f"the mean of the actual: {np.mean(result): .3f}")


error = result - bl
meanerror =  np.mean(error)
stderror = np.std(error)
print(f"the mean error: {meanerror: .2f}")
print(f"the standard deviation: {stderror: .2f}")


#from random import normal #not recommended 
#import random.normal as rnnorm
y = np.random.normal(meanerror, stderror, 1000)#y = normalapprox = np.random.normal(meanerror, stderror, 1000)
#xaxis = np.linspace(-20,20,100)

plt.hist(y, density = True)


## HW = put all 3 graphs on one grapph give legend and alpha 
plt.hist(bl, alpha = 0.5, label = 'line', density = True)
plt.hist(result, alpha = 0.25, label = 'actual', density = True)
plt.hist(y, alpha = 0.75, label = 'error', density = True)
plt.legend()
plt.grid()
plt.show() 

## if we always bet on the home team 
type(bl)
bllist = list(bl)
size = len(bllist)
actlist = list(result)

#betting on the home team
total = 0
for x in range(size):
    if (bllist[x] + actlist[x] > 0):
        total += 10
        
    else:
        total -= 11

print(total)


#betting on visiting team
total = 0
for x in range(size):
    if (bllist[x] + actlist[x] < 0):
        total += 10
        
    else:
        total -= 11

print(total)


















