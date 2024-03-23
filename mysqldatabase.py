import pymysql 
myobj=pymysql.connect(host="localhost" , user="root" , passwd='')
cur=myobj.cursor()
try:
    cur.execute("create database school")
    print ("DataBase successfully created.")
except Exception as e:
    print ("Error",e)