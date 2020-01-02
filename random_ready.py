# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:49:34 2019
Uses choas.tools random number generation to create a binary
file of random bytes

@author: Thomas
"""
from choas import tools

"""
minimum is smallest byte value, max_seed is equal to the maximum
byte value+minimum, number is number of bytes to write to the file
"""
def implant(file,minimum=0,number=100,max_seed=100):
   values = []
   for i in range(number):
       values.append(minimum+tools.random(max_seed))
   with open(file,"wb") as f:
       for i in range(number):
           f.write(bytes(values))



