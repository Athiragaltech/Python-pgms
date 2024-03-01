#frequency of number
t=(4,3,9,8,2,10,10)
unique=set(t)
for item in unique:
    print(f" count of {item} in tuple t:{t.count(item)}")

#set creation
a={1,2,3,4,}
b={10,20,30,40}
print("set is" ,a)
print("second set is",b)

#insertion in set
x={"ammu","anju","annu"}
print("set is",x)
x.add("lechu")
print("Aftr insertion",x)

#remove item
y={"arun","lallu","lechu"}
print("set is",y)
y.remove("arun")
print("aftr removal",y)

#set intersection
m={"apple","orange","plum"}
print("first set",m)
n={"cherry","banana","orange"}
print("second set",n)
q=m.intersection(n)
print("aftr intersection",q)

#set union
c={10,20,30}
print("first set is",c)
d={80,90,70}
print("second set is",d)
l=c.union(d)
print("resultant set is",l)


#set difference
k={"one","two","three"}
print("first set",k)
f={"five","one","three"}
print("second set is",f)
l=k.difference(f)
print("resultant set is",l)

#copy of set
x = {"apple", "banana", "cherry"}
print(x)
y = {"google", "microsoft", "apple"}
print(y)
z = x.union(y)
print(z)

#set removal
x = {"apple", "banana", "cherry"}
x.clear()









































