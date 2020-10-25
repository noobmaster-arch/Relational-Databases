import sqlite3
import csv

conn=sqlite3.connect('ipl.db')

cur=conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS POINTS_TABLE(
    team_id INT PRIMARY KEY,
    team_name TEXT,
    points INT,
    nrr DECIMAL
);''')
cur.execute('''
                INSERT INTO POINTS_TABLE(team_id, team_name, points, nrr)
                SELECT team_id, team_name, team_id*0, team_id*0
                FROM TEAM                
                ;''')
cur.execute("""
                UPDATE POINTS_TABLE
                SET 
                    points = 2*(SELECT COUNT(*)
                                FROM MATCH
                                WHERE POINTS_TABLE.team_id = MATCH.match_winner AND MATCH.win_type != 'Tie'
                                )
            ;""")
cur.execute("""
                UPDATE POINTS_TABLE
                SET 
                    points = points + (SELECT COUNT(*)
                                FROM MATCH
                                WHERE POINTS_TABLE.team_id = MATCH.team1 AND ( MATCH.win_type == 'Tie' OR MATCH.match_winner == "NULL" )
                                )
            ;""")
cur.execute("""
                UPDATE POINTS_TABLE
                SET 
                    points = points + (SELECT COUNT(*)
                                FROM MATCH
                                WHERE POINTS_TABLE.team_id = MATCH.team2 AND ( MATCH.win_type == 'Tie' OR MATCH.match_winner == "NULL" )
                                )
            ;""")







cur.execute("""
                UPDATE POINTS_TABLE
                SET 
                    nrr = nrr + 0.05*(SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team1 AND MATCH.win_type == "runs" AND MATCH.team1 == MATCH.match_winner )
                WHERE (SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team1 AND MATCH.win_type == "runs" AND MATCH.team1 == MATCH.match_winner ) IS NOT NULL
            ;""")

cur.execute("""
                UPDATE POINTS_TABLE
                SET 
                    nrr = nrr - 0.05*(SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team1 AND MATCH.win_type == "runs" AND MATCH.team1 != MATCH.match_winner )
                WHERE (SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team1 AND MATCH.win_type == "runs" AND MATCH.team1 != MATCH.match_winner ) IS NOT NULL
            ;""")

cur.execute("""
                UPDATE POINTS_TABLE
                SET 
                    nrr = nrr + 0.05*(SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team2 AND MATCH.win_type == "runs" AND MATCH.team2 == MATCH.match_winner )
                WHERE (SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team2 AND MATCH.win_type == "runs" AND MATCH.team2 == MATCH.match_winner ) IS NOT NULL
            ;""")

cur.execute("""
                UPDATE POINTS_TABLE
                SET 
                    nrr = nrr - 0.05*(SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team2 AND MATCH.win_type == "runs" AND MATCH.team2 != MATCH.match_winner )
                WHERE (SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team2 AND MATCH.win_type == "runs" AND MATCH.team2 != MATCH.match_winner ) IS NOT NULL
            ;""")






cur.execute("""
                UPDATE POINTS_TABLE
                SET 
                    nrr = nrr + 0.1*(SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team1 AND MATCH.win_type == "wickets" AND MATCH.team1 == MATCH.match_winner )
                WHERE (SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team1 AND MATCH.win_type == "wickets" AND MATCH.team1 == MATCH.match_winner ) IS NOT NULL
            ;""")

cur.execute("""
                UPDATE POINTS_TABLE
                SET 
                    nrr = nrr - 0.1*(SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team1 AND MATCH.win_type == "wickets" AND MATCH.team1 != MATCH.match_winner )
                WHERE (SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team1 AND MATCH.win_type == "wickets" AND MATCH.team1 != MATCH.match_winner ) IS NOT NULL
            ;""")

cur.execute("""
                UPDATE POINTS_TABLE
                SET 
                    nrr = nrr + 0.1*(SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team2 AND MATCH.win_type == "wickets" AND MATCH.team2 == MATCH.match_winner )
                WHERE (SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team2 AND MATCH.win_type == "wickets" AND MATCH.team2 == MATCH.match_winner ) IS NOT NULL
            ;""")

cur.execute("""
                UPDATE POINTS_TABLE
                SET 
                    nrr = nrr - 0.1*(SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team2 AND MATCH.win_type == "wickets" AND MATCH.team2 != MATCH.match_winner )
                WHERE (SELECT SUM(win_margin) FROM MATCH WHERE POINTS_TABLE.team_id = MATCH.team2 AND MATCH.win_type == "wickets" AND MATCH.team2 != MATCH.match_winner ) IS NOT NULL
            ;""")



# cur.execute("""
#                 UPDATE POINTS_TABLE
#                 SET 
#                     points = points + 0.1*(SELECT SUM(win_margin)
#                                 FROM MATCH
#                                 WHERE POINTS_TABLE.team_id = MATCH.match_winner AND MATCH.win_type == "wickets" 
#                                 )
#             ;""")

conn.commit()




cur.execute("""
                SELECT *
                FROM POINTS_TABLE
                ORDER BY
                    points DESC, nrr DESC
;""")
for i in cur.fetchall():
    print("{},{},{},{}".format(i[0], i[1], i[2], i[3]))
conn.close()