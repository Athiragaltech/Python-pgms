import pymysql
db=pymysql.connect(host='localhost',user='root',password="ammu",database="college")
cursor=db.cursor()
cursor.execute("""create table class(sid int,name varchar(255),class varchar(255),coll varchar(255))""")
print("Table created")
db.close()
