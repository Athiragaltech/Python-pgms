#Sort dictionary

dic={2:90, 1: 100, 8: 3, 5: 67, 3: 5}
dic2={}
for i in sorted(dic):
   dic2[i]=dic[i]
print(dic2)

#add,update,delete operations in dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
print(car)

car.update({"color": "White"})

print(car)

car.pop("model")
print(car)

#concatination
d1 = {'A': 15, 'B': 10, 'C' : 12 }  
d2 = {'E': 18,'B': 20,'D' : 16 }  
d1.update(d2)  
print('Updated dictionary:')  
print(d1)

#forloop

dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}
for key in dt:
    print(key, dt[key])
    
#merging
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)































print(dict_1 | dict_2)
