import sqlite3
conn=sqlite3.connect("sqlite.db")

selectQuerry="DELETE FROM Student where st_id='4'"
StudentTuple=conn.execute(selectQuerry)
conn.commit()