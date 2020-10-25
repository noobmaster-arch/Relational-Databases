import sqlite3
import csv

conn=sqlite3.connect('ipl.db')

with conn:
    cur=conn.cursor()
    cur.execute(""" 
                    CREATE TEMP VIEW IF NOT EXISTS numberofsixes (
                        sixes,
                        player__id
                    )
                    AS
                        SELECT
                            COUNT(*), PLAYER.player_id
                        FROM BALL_BY_BALL
                        INNER JOIN PLAYER ON PLAYER.player_id = BALL_BY_BALL.striker
                        WHERE
                            runs_scored == 6
                        GROUP BY
                            PLAYER.player_id
                    ;""")
    cur.execute(""" 
                    CREATE TEMP VIEW IF NOT EXISTS numberofballs (
                        balls,
                        player__id,
                        player__name
                    )
                    AS
                        SELECT
                            COUNT(*), PLAYER.player_id, player_name
                        FROM BALL_BY_BALL
                        INNER JOIN PLAYER ON PLAYER.player_id = BALL_BY_BALL.striker
                        GROUP BY
                            PLAYER.player_id
                    ;""")
    cur.execute("""
                    SELECT
                        numberofballs.player__id, player__name, sixes, balls, sixes*1.0/balls
                    FROM numberofballs INNER JOIN numberofsixes ON numberofballs.player__id = numberofsixes.player__id
                    ORDER BY
                        sixes*1.0/balls DESC, player__name ASC
    
                    ;""")

    
    one_result = cur.fetchall()
    for i in one_result:
        print("{},{},{},{},{}".format(i[0], i[1], i[2], i[3], i[4]))
    
    cur.execute("""DROP VIEW IF EXISTS numberofsixes;""")
    cur.execute("""DROP VIEW IF EXISTS numberofballs;""")

    