f=open("myfiles.txt","w")
name=input("Enter Empname  :")
f.write(name)
class1=input("Enter Department  :")
f.write(class1)
sch=input("Enter Designation  :")
f.write(sch)
f=open("myfiles.txt","r")
print(f.read())
f.close()