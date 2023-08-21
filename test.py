import template 


w1 = template.workout(1,4,5,["set1"])

print(w1.date)

w1.add_set(13, 44)


print(w1.export())

#printing the value of "keys"


diction= {"a":2, "b":4, "c":6}

#printing all keys
keys=list(diction.keys())

list1=["set1","set2"]
last_element=int(list1[-1][-1])
print(type(last_element))

