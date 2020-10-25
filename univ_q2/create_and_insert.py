import sqlite3 as lite
import sys

con=lite.connect('univ.db')
with con:
    cur=con.cursor()
    with open('University Schema','r') as f:
        script=f.read().split(';')
        for scr in script:
            try:
                cur.execute(scr)
            except:
                pass

    with open('smallRelationsInsertFile.sql','r') as d:
        data=d.read().split(';')
        for dat in data:
            try:
                cur.execute(dat)
            except:
                pass

