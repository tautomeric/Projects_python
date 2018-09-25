# -*- coding: utf-8 -*-
"""
Measures the number of times an operation can be done in a second, and 
as such can be used to estimate processing speed
@note: Though having the same algotherm, but for microseconds instead of 
seconds would improve run time, the sample space would also be smaller and
more susceptible to random fluctuations.
@author: Thomas
"""
import counter

def speed_count():
 counter.second_count()
 return counter.second_count()


