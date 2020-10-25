import sqlite3
import csv

conn=sqlite3.connect('ipl.db')

with conn:
    cur=conn.cursor()
    cur.execute("""
                    SELECT
                        c1.venue_name, AVG((SELECT SUM(runs_scored + extra_runs) FROM BALL_BY_BALL c2 WHERE c2.match_id=c1.match_id GROUP BY match_id)) as avera
                    FROM MATCH c1
                    WHERE
                        c1.venue_name != "NULL"
                    GROUP BY
                        c1.venue_name
                    ORDER BY
                        avera DESC, c1.venue_name ASC                  
    ;""")
    one_result = cur.fetchall()
    for i in one_result:
        print("{},{}".format(i[0], i[1]))

    