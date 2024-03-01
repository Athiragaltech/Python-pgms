import pymysql
db=pymysql.connect(host='localhost',user='root',password="ammu",database="college")
cursor=db.cursor()

ins="insert into class(sid,name,class,coll)values(%d,%s,%s,%s)"
sid=int(input("enter id"))
name=input("Enter name")
class1=input("enter class")
coll=input("enter college")
data=(sid,name,class1,coll)
try:
  cursor.execute(ins,data)
  db.commit()
  print("Inserted")
except:
  db.rollback()
  print("Err")
db.close()
