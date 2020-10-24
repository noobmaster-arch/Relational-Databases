import sqlite3
import csv

conn=sqlite3.connect('ipl.db')

with conn:
    cur=conn.cursor()
    cur.execute("""

                        SELECT
                            SUM(runs_scored) + SUM(extra_runs), venue_name FROM BALL_BY_BALL INNER JOIN MATCH ON MATCH.match_id = BALL_BY_BALL.match_id
                        GROUP BY
                            BALL_BY_BALL.match_id

                        ORDER BY
                            SUM(runs_scored) DESC
                    ;""")
    one_result = cur.fetchall()
    for i in one_result:
        print("{},{}".format(i[1], i[0]))

    