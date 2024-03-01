#max of 3 numbers

a=int(input("enter first num"))
b=int(input("enter second number"))
c=int(input("enter last number")) 
def maximum(a, b, c): 
   
    if (a >= b) and (a >= c): 
        largest = a 
 
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
         
    return largest

print (maximum(a,b,c))


#replacing a word

text = 'Hello, World!'
new_text = text.replace('World', 'Python')
print(new_text)





    
