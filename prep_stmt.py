import sys
import sqlite3
conn=sqlite3.connect('ipl.db')
cur=conn.cursor()
if(int(sys.argv[1])==1):
    cur.execute("INSERT INTO TEAM VALUES (?, ?);", sys.argv[2:])
if(int(sys.argv[1])==2):
    cur.execute("INSERT INTO PLAYER VALUES (?, ?, ?, ?, ?, ?);", sys.argv[2:])
if(int(sys.argv[1])==3):
    cur.execute("INSERT INTO MATCH VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", sys.argv[2:])
if(int(sys.argv[1])==4):
    cur.execute("INSERT INTO PLAYER_MATCH VALUES (?, ?, ?, ?, ?, ?, ?);", sys.argv[2:])
if(int(sys.argv[1])==5):
    cur.execute("INSERT INTO BALL_BY_BALL VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", sys.argv[2:])
conn.commit()