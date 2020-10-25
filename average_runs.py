import sqlite3
import csv

conn=sqlite3.connect('ipl.db')

with conn:
    cur=conn.cursor()
    cur.execute(""" CREATE TEMP VIEW IF NOT EXISTS looks (
                        runs,
                        venue
                    )
                    AS
                        SELECT
                            SUM(runs_scored) + SUM(extra_runs), venue_name FROM BALL_BY_BALL INNER JOIN MATCH ON MATCH.match_id = BALL_BY_BALL.match_id
                        GROUP BY
                            BALL_BY_BALL.match_id

                        ORDER BY
                            SUM(runs_scored) DESC
                    ;""")

    cur.execute("""
                    SELECT
                        AVG(runs), venue
                    FROM
                        looks
                    GROUP BY
                        venue
                    ORDER BY
                        AVG(runs) DESC, venue ASC
                    
    ;"""
    )
    one_result = cur.fetchall()
    for i in one_result:
        print("{},{}".format(i[1], i[0]))
    cur.execute("""DROP VIEW IF EXISTS looks;""")

    