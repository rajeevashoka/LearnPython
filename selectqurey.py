import sqlite3
conn=sqlite3.connect("sqlite.db")
selectQuerry='''
            select * from Student 
'''
#selectQuerry="DELETE FROM Student where st_id=4"
StudentTuple=conn.execute(selectQuerry)
#conn.commit()

print (StudentTuple)
for row in StudentTuple:
    print (row)
