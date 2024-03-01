#10 numbers
lst = []
print("Enter 10 numbers : ")
for i in range(0, 10):
    ele = int(input())
    lst.append(ele)  
 
print(lst)



#occurance
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
lst = [8, 6, 9, 10, 8, 20, 10, 9, 8]
x = 9
print('{} has occurred {} times'.format(x,
                                        countX(lst, x)))


#largest and smallest number
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))


#list of fruits
l=["apple","orange","grapes","pine apple"]
x=list(l)
print(x)

#length of list
ab = ['Python', 'Java', 'Ruby', 'JavaScript']
size = len(ab)
print(size)

#reverse of list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#squaring list elements
list_nums= [1, 2, 3, 4, 5]

for i, v in enumerate(list_nums):
   list_nums[i] = v**2

print(list_nums)

#numbers divisible by 5
my_list = [10, 65, 54, 39, 102, 330, 221]
result = list(filter(lambda x: (x % 5 == 0), my_list))
print("Numbers divisible by 13 are",result)

#sum of list
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(total)

#odd an deven
nums = [43, 20, 53, 12, 53, 5, 3, 2]
even = []
odd = []
for i in nums:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
       
print("Even List: ",even)
print("Odd List: ",odd)
































 
