# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:55:39 2019
-__init__ takes in specification as a dictionary wherein each key represents a
catagory and each value the maximum possible value in that catagory
-catagories method takes in an array of numbers (a) and notes the number of 
values in a within each catorgory 
  
@author: Thomas
"""
import numpy as np
class catorgories:
    def __init__(self,cat_specs={"defualt":0}):
        self.cat_specs = cat_specs
        
    def catagorize(self,values=np.array([0],dtype="int8")):
        local = 0
        values.sort()
        num_in_cats = self.cat_specs.copy()
        last_local = len(values)
        
        for i in self.cat_specs: 
            max_in = self.cat_specs[i]
            num_of = 0
            while(values[local]<=max_in):
                num_of = num_of + 1
                local = local+1
                if(last_local<=local):
                    break
                
            num_in_cats[i] = num_of
        return num_in_cats

    def get_catagory_num(self,catagory):
        return self.num_in_cats[catagory]

import math
from datetime import datetime
class tools:
    #returns the ceiling of n/e
    def stop_point(n):
        stop_point = 0
        
        if type([]) == type(n):
            stop_point = math.ceil(len(n)/math.e)
        elif type(2)==type(n):
            stop_point = math.ceil(n/math.e)
        else:
            raise TypeError("stop_point must receive either an int or list")
        
        return stop_point
   
    #finds the optimal stopping point in a list based on the solution to the
    #secretary problem. Includes a "negative" option to find the optimal minimum
    def guess_stop(choices,negative=False):
        num_choices = len(choices)-1
        start_point = math.ceil(num_choices/math.e)
        guess = choices[start_point]
        
        if negative:
            while start_point <= num_choices:
                if guess>choices[start_point]:
                    guess = choices[start_point]
                    break
                start_point += 1
        else:
            while start_point <= num_choices:
                if guess<choices[start_point]:
                    guess = choices[start_point]
                    break
                start_point += 1
        return guess
    
    def _counter(time="second"):
        if time == "second":
            timebank = datetime.now()
            starttime = timebank.second
            endTime = timebank.second
            count = 1
            while starttime == endTime:
                timeBank2 = datetime.now()
                endTime = timeBank2.second
                count = count + 1
            return count 
        else:
            timebank = datetime.now()
            starttime = timebank.microsecond
            endTime = timebank.microsecond
            count = 1
            while starttime == endTime:
                timeBank2 = datetime.now()
                endTime = timeBank2.microsecond
                count = count + 1
            return count 
        
    #returns a number coorsponding to the speed the computer is running at
    def speed_count():
        tools._counter()
        return tools._counter()  
    
    #returns a random number
    def random(max_seed):
        a = tools._counter(time=0)
        if (a > (a % max_seed)):
            return a % max_seed
        else:
            return max_seed % a
              
