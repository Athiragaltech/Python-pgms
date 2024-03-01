from stud import studetails,markdetails
studetails.stud("ammu",10,"LF")
 



print("How many students marks you want to enter: ")
n = int(input())
for i in range(0,n):
 print("Enter marks of student",(i+1),":")
 marks = int(input())
 list1.append(marks)
 
average = computeAverage(list1,n)
print("Average marks of",n,"students is:",average)

markdetails.computeAverage(list1,n)
   
