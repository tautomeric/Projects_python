# -*- coding: utf-8 -*-
"""
Returns a random positive int no larger than a given value
@author: Thomas
"""
import counter

def random(max_seed):
 a = counter.microsecond_count()
 if (a > (a % max_seed)):
     return a % max_seed
 else:
     return max_seed % a
 
