import sqlite3
conn=sqlite3.connect("sqlite.db")


insertQuerry='''
            insert into Student (st_name,st_class,st_email) VALUES ('RAJEEV','12th','rajeev@gmail.com')
'''
conn.execute(insertQuerry)
conn.commit()
conn.close()
