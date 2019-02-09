# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 07:11:16 2019
Checks the randomness of interger pseudo-random number generators

@author: Thomas
"""
import numpy as np
import matplotlib.pyplot as plt
import math

numbers = input("Input numbers as follows: 1,2,3...")

data = numbers.split(",")
data_len = len(data)
#ensures sample of significance size
if data_len < 25:
    raise ValueError("Sample must have at least 25 items")

for i in range(data_len):
  data[i] = int(data[i])

data = np.array(data)

denom = np.max(data)
#hold varience away from expected randomness
random = []
ones = data[0]
ones_number = 0
for i in range(data_len):
 if data[i] == ones:
     ones_number = ones_number + 1
 
 random.append(abs(1/denom-i/ones))
#finds and graphs 
random = np.array(random)
print("Average variation away from expected randomness:",np.mean(random),"\n") 
print()

plt.title("Variation away from expected random over time:")
plt.plot(random,color = '#563457')

#finds a model to desribe randomness variation over time
model = ""
j = 1 
k = 0  
checker = 1000;      
for i in range(20):
    
   check_models = []
   
   
   for i in range(data_len):
    check_models.append(abs(random[i]-math.sin((i+1)*j)/((i+1)*j)))
    
 
   
   temp = np.mean(check_models)
   if checker < temp:
       checker = temp
       k = j
       print (j)
   if i == data_len-1:
       k = str(k)
       model = "sin" + k+"x/" + "x" + k
       
   j = j+1
   
if model[3] == str(0):
    print("***No good descending sin model for data***")
else:
    print(model + " is a good model for data")
    
"""
Project designed for ugahacks4
"""
   
