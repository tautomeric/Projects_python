# -*- coding: utf-8 -*-
"""
Modified version of portmanteauanalyizer for samples with larger seperations

@author: Thomas
"""
import numpy as np
import portmanteau as p

class sample_comparer:
 def __init__(self,data):
  placer = data.split(" ")
  data_length = int(placer[0])
  placer.pop(0)

  #holds data of "front" and "back word" from part_find
  front_form = []
  back_form = []
  #holds data of "front" and "back word" from percent_find
  front_percent = []
  back_percent = []
  #holds data of "front" and "back word" from percent_word
  front_word = []
  back_word = []

  for i in range(data_length):
   entry = p.portmanteau(placer[i],placer[i+1],placer[i+2])
    
   front_form.append(entry.name_1)
   back_form.append(entry.name_2)
   front_percent.append(entry.percent_find()[0])
   back_percent.append(entry.percent_find()[1])
   front_word.append(entry.percent_word()[0])
   back_word.append(entry.percent_word()[1])
     
    
  #specified dtype removed 
  self.front_form_data = np.array([front_form])   
  self.back_form_data = np.array([back_form])  
  self.front_percent_data = np.array([front_percent])  
  self.back_percent_data = np.array([back_percent])  
  self.front_word_data = np.array([front_word])  
  self.back_word_data = np.array([back_word]) 


 def number_letters_mean(self):
     rtrn = [1,2]
     rtrn[0] = self.front_form_data.mean()
     rtrn[1] = self.back_form_data.mean()
     return rtrn
     
 def number_letters_std(self):
     rtrn = [1,2]
     rtrn[0] = self.front_form_data.std()
     rtrn[1] = self.back_form_data.std()
     return rtrn 

 def percent_portmanteau_mean(self):
     rtrn = [1,2]
     rtrn[0] = self.front_percent_data.mean()
     rtrn[1] = self.back_percent_data.mean()
     return rtrn 
 
 def percent_portmanteau_std(self):
     rtrn = [1,2]
     rtrn[0] = self.front_percent_data.std()
     rtrn[1] = self.back_percent_data.std()
     return rtrn

 def percent_word_mean(self):
     rtrn = [1,2]
     rtrn[0] = self.front_word_data.mean()
     rtrn[1] = self.back_word_data.mean()
     return rtrn
 
 def percent_word_std(self):
     rtrn = [1,2]
     rtrn[0] = self.front_word_data.std()
     rtrn[1] = self.back_word_data.std()
     return rtrn
