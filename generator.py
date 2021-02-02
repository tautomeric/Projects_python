# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 07:34:11 2020

@author: tburl
"""
import choas as c
import numpy as np

def _find_sigs(entries):
        most=0
        for i in entries:
            check=str(i)
            if(len(check)>most):
                most=len(check)
        return most-2

    
def _form_rule(entries):
       
        magnatude=_find_sigs(entries)
        fixing_number=10**magnatude
        
        next_point=fixing_number
        find_block=[]
        for i in entries:
            next_point-=i*fixing_number
            find_block.append(int(next_point))
            
            
        return([fixing_number,find_block])

def _get_next_num(rule):
    
    find=c.tools.random(rule[0])
    
    for i in range(len(rule[1])):
        n=int(len(rule[1])/2)
        check=int(rule[1][n])
        
        if check==find:
            return n
        elif check<find:
            end=int(rule[1][n-1])
            if end>find:
                return n
            else:
                n=int(n/2)
        elif check>find:
            end=int(rule[1][n+1])
            if end<find:
                return n+1
            else:
                n+=int(n/2)
    return 0
    
class generator():
    
   def __init__(self,specs):
        self.generator=[]
        
        for i in specs:
            if(np.sum(i)!=1):
                massage="a sum in the specs does not equal 1"
                raise ValueError(massage)

            else:
              self.generator.append(_form_rule(i))
      
   
              
   def run(self,rounds=1000):
        result=[]
        iters=0
        new_num=c.tools.random(len(self.generator))
              
        while iters<rounds:
            result.append(new_num)
            
            new_num=_get_next_num(self.generator[new_num])
            
            iters+=1
        
        return result
       
if __name__=="__main__":
    a=generator([[.5,.5],[.34,.66]])
    