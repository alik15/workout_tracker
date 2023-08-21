import datetime
import json
import pandas as pd



#check if workout data exists 
#else make it

#read workout data from file 

# JSON file
f = open ('workouts.json', "r")
 
# Reading from file
data = json.loads(f.read())
print(data)
 

#Add new workout 
def add_workout():
    
    w1 = template.workout(1,4,5,["set1"])



#Add new set

#write workout to file json