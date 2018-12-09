# -*- coding: utf-8 -*-
"""
@author: Thomas
"""


class portmanteau:
   
 #Finds the number of letters each word contributes to a "regular" portmanteau.    
 def __init__(self,c,a,b):
     
     i = 0
     while c[i] == a[i]:
         i = i+1
         if i == len(a):
             break
         
     self.c = len(c)
     self.a = len(a)
     self.b = len(b)
     self.name_1 = i
     self.name_2 = self.c - i
     
     
 # finds percent that each word contributes 
 def percent_find(self):
     
     rtrn = []
     
     rtrn.append(100*(self.name_1/self.c))
     rtrn.append(100 - rtrn[0])
     
     return rtrn
 # finds what percent of each word is used
 
 def percent_word(self):
    
     rtrn = []
     rtrn.append(100*(self.name_1/self.a))
     rtrn.append(100*(self.name_2/self.b))
     
     return rtrn



