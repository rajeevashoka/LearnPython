import pymysql 
mydb=pymysql.connect(host="localhost" , user="root" , passwd="",database="school")
cur=mydb.cursor()
try:
    insertQuerry="insert into student (st_name,st_class,st_email) VALUES (%s,%s,%s)"
    t=('SONU','12th','sonu@gmail.com')
    cur.execute(insertQuerry,t)
    mydb.commit()
    print(cur.rowcount, "record(s) affected")
    cur.close()
except Exception as e:
    print ("Error",e)

