import numpy as np

class catorgories:
    def __init__(self,cat_specs={"defualt":0}):
        self.cat_specs = cat_specs
         
    def catagorize(self,values=np.array([0],dtype="int8")):
        local = 0
        values.append(0)
        values.sort()
        num_in_cats = self.cat_specs.copy()
        last_local = len(values)-1
        
        for i in self.cat_specs: 
            max_in = self.cat_specs[i]
            num_of = 0
            while(values[local]<=max_in):
                if(last_local<=local):
                    break
                num_of = num_of + 1
                local = local+1
                
            
            num_in_cats[i] = num_of
       
        self.num_in_cats = num_in_cats
        return num_in_cats
    
    
    def get_catagory_num(self,catagory):
        return self.num_in_cats[catagory]

    def max_cat(self):
        most = 0
        cat = 0
        
        for i in self.num_in_cats:
            if self.num_in_cats[i]>=most:
                most = self.num_in_cats[i]
                cat = i
        return cat
    
    def min_cat(self):
        most = 0
        cat = 0
        
        for i in self.num_in_cats:
            if self.num_in_cats[i]<=most:
                most = self.num_in_cats[i]
                cat = i
        return cat
    
import math
from matplotlib import pyplot as plt
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
     #returns an array with data for a wave with psuedorandom interferance 
     #also can (see_wave=True) print a graph of a random wave.
    def random_wave(see_wave=False):
        cut_points = np.random.randint(2000,4000,2)
        cut_points.sort()
        disbute = np.random.normal(4,43,4000)
        wave = disbute[cut_points[0]:cut_points[1]]
        
        if see_wave:
            plt.plot(wave)
            plt.fill()
        
        return wave

    #returns when number of integer jumps until lambda a excedes lambda b
    #errors to add when used: that the equations do not intersect at any point
    def met_point(a=lambda o:o,b=lambda o:math.log2(o),i=1):
        while a(i)< b(i):
            i+=1
        return i
    
    def probable_same(a=lambda o:o,b=lambda o:math.log2(o),trials=100):
        same=True
        most=0
        for i in range(trials):
            test_value=tools.random(100)+most
            print(test_value)
            most=test_value+1
            if(a(test_value)!=b(test_value)):
                same=False
                break
        return same
    
    def blind_prob(data=[1,1,2],win=1):
        wins=0
        for i in data:
            if i==win:
                wins+=1
                
        return (wins+1)/(len(data)+2)
