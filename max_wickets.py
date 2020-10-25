import sqlite3
import csv

conn=sqlite3.connect('ipl.db')

with conn:
    cur=conn.cursor()
    cur.execute("""

                        SELECT
                            COUNT(*), PLAYER.player_id, player_name
                        FROM BALL_BY_BALL
                        INNER JOIN PLAYER ON PLAYER.player_id = BALL_BY_BALL.bowler
                        WHERE
                            out_type != "Not Applicable"
                        GROUP BY
                            PLAYER.player_id
                        ORDER BY
                            COUNT(*) DESC, player_name ASC
                    ;""")
    one_result = cur.fetchmany(20)
    for i in one_result:
        print("{},{},{}".format(i[1], i[2], i[0]))

    