import sqlite3 as lite
import sys

con=lite.connect('univ.db')
cur=con.cursor()
if int(sys.argv[1]) is 0:
    query="SELECT *  FROM " + sys.argv[2]+ " WHERE " + sys.argv[3] + " = " + "'" + sys.argv[4] + "'"
    try:
        cur.execute(query)
        rows=cur.fetchall()
        for row in rows:
            st=','.join(str(x) for x in row)
            print(st)
    except:
        pass
    

else:
    try:
        query='SELECT * FROM %s WHERE  %s =?' %(sys.argv[2], sys.argv[3])
        cur.execute(query,(sys.argv[4],))
        rows=cur.fetchall()
        for row in rows:
            st=','.join(str(x) for x in row)
            print(st)
    except :
        pass
con.close()
