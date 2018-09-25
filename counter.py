# -*- coding: utf-8 -*-
"""

@author: Thomas
"""
from datetime import datetime

 

def second_count():
  timebank = datetime.now()
  starttime = timebank.second
  endTime = timebank.second
  count = 1
  while starttime == endTime:
 
   timeBank2 = datetime.now()
   endTime = timeBank2.second
   count = count + 1
  return count 

def microsecond_count():
  timebank = datetime.now()
  starttime = timebank.microsecond
  endTime = timebank.microsecond
  count = 1
  while starttime == endTime:
 
   timeBank2 = datetime.now()
   endTime = timeBank2.microsecond
   count = count + 1
  return count 