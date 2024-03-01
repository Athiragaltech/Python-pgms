#voting eligibility
ag=int(input("Enter age"))
if (ag>18):
    print("eligible for vote")
else:
    print("not eligible")
    
#num is zero,negative or positive
num=int(input("Enter number"))
if(num==0):
    print("number is zero")
elif(num>0):
    print("number is positive")
else:
    print("number is negative")

        
#for loop
for i in range(-10,0):
    print(i)

#for loop
for i in range(200,500,2):
    print(i)


number = int(input("\nEnter number: "))
print("The multiples are: ")
for i in range(1,100):
    print(number*i, end =" ")
    
    

num = int(input("\nEnter a number: "))
print("The multiplication table is as follows:")
for i in range(1,11):
    print("{} x {} = {}".format(num,i, num*i))


hello_world = "\nHello World"

for char in hello_world:
    if char.lower() == 'w':
        continue  
    print(char, end=' ')


welcome_message = "\n welcome\n"

for char in welcome_message:
    print(char, end=' ')
    if char.lower() == 'c':
        break


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in range(1, len(my_list), 2):
    print(my_list[index], end=' ')    


























    
