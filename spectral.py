# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:41:57 2019

@author: Thomas
"""
import numpy as np
import choas
class spectrum:
    def __init__(self,a=0,b=0,q=0):
         if (b-a)%q != 0:
             raise ValueError("Invalid values for spectrum")
         
         self.a = a
         self.b = b
         self.q = q
         self.spectrum = []
        
         start = a
         self.spectrum_skeleton = {}
        
         while start <= b:
            self.spectrum.append(start)
            self.spectrum_skeleton.update({start:start})
            start = start + q
            
    def list_ceiling(self,data=np.array([0],dtype=np.int8)):
       
        end = np.size(data) 
        locale = 0
        while locale<end:
            check = data[locale]
            
            if(check<self.a or check >self.b ):
                data = np.delete(data,locale)
                end = end - 1
            else:
                locale = locale + 1
       
        
        list_ceiling = choas.catorgories(self.spectrum_skeleton)
        processed = data
        return list_ceiling.catagorize(processed) 
    
    def list_floor(self,data=np.array([0],dtype=np.int8)):
        end = np.size(data) 
        locale = 0
        while locale<end:
            check = data[locale]
            
            if(check<self.a or check >self.b ):
                data = np.delete(data,locale)
                end = end - 1
            else:
                locale = locale + 1
        
        negative_clone = self.spectrum_skeleton.copy()
        negative_clone = sorted(negative_clone,reverse=True)
        
        inverse_skeleton={}
        for i in negative_clone:
            inverse_skeleton.update({i:-i})
        
        negative_data = []
        iters = np.size(data)
        
        for i in range(iters):
           negative_data.append(-data[i])
            
        list_floor = choas.catorgories(inverse_skeleton)
        return list_floor.catagorize(negative_data)
        
    
    def spectrum_floor(self,n):
        if self.a <= n<=self.b:
            left_side = 0
            right_side = len(self.spectrum) - 1
            m = int((left_side + right_side) / 2)
            while left_side <= right_side:
                if self.spectrum[m] < n:
                    left_side= m + 1
                elif self.spectrum[m] > n:
                    right_side = m - 1
                else:
                    break
                m = int((left_side + right_side) / 2)
            
            return self.spectrum[m]
        else:
            return None
       
        
    def spectrum_ceiling(self,n):
      
        if self.a <= n<=self.b:
            for i in self.spectrum:
                if(i>=n):
                  return i  
        else:
            return None
             
a = spectrum(2,10,2)
b = np.array([1,2,3,3,4,4,5,5,10]) 
     
for i in range(len(b)):
   print(a.spectrum_floor(b[i]))




        
           
        
        