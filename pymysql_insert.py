import pymysql
db=pymysql.connect(host='localhost',user='root',password="ammu",database="college")
cursor=db.cursor()
ins_stmt="insert into emp(name)values(%s)"
name=input("enter name")
data=(name)
try:
    cursor.execute(ins_stmt,data)
    db.commit()
    print("inserted")
except:
    db.rollback()
    print("err")
db.close()    
