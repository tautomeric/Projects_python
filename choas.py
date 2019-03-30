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

