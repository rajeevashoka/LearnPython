import pymysql 
myobj=pymysql.connect(host="localhost" , user="root" , passwd="",database="school")
cur=myobj.cursor()

tablecreate="CREATE TABLE student (st_id INT PRIMARY KEY AUTO_INCREMENT,st_name varchar(50),st_class varchar(10), st_email varchar(50))"
cur.execute(tablecreate)
print(cur.rowcount, "record(s) affected")

