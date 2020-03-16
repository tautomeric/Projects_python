# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:44:47 2020

@author: Thomas
"""
class _wrapper:
    def __init__(self,item,prev=None,nextIt=None):
        self.prev=prev
        self.nextIt=nextIt
        self.item=item
               
class stackqueue:
    
    def __init__(self):
        self.head=_wrapper(None)
        self.tail=_wrapper(None)
        self.head.nextIt=self.tail
        self.tail.prev=self.head
    
    def is_empty(self):
        if(self.head.nextIt==self.tail):
            return True
        return False
        
    def add(self,item):
        newItem=_wrapper(item)
        newItem.nextIt=self.head.nextIt
        newItem.prev=self.head
        self.head.nextIt.prev=newItem
        self.head.nextIt=newItem
        
    def print_items(self):
        to_print=self.head.nextIt
        
        while(to_print.item!=None):
            print(to_print.item)
            to_print=to_print.nextIt
            
    def length(self):
        to_print=self.head.nextIt
        size=0
        
        while to_print.item!=None:
            size+=1
            to_print=to_print.nextIt
        return size
        
    def stack_pop(self):
        if(self.is_empty()):
            raise RuntimeError("Data structure is empty")
        else:
            self.head.nextIt=self.head.nextIt.nextIt
            
    def queue_pop(self):
        if(self.is_empty()):
            raise RuntimeError("Data structure is empty")
        else:
            self.tail.prev=self.tail.prev.prev
            self.tail.prev.nextIt=self.tail
            

    
    