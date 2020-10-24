import sqlite3
import csv

conn=sqlite3.connect('ipl.db')

cur=conn.cursor()
csvReader = csv.reader(open('team.csv'))
next(csvReader)
for row in csvReader:
    cur.execute('insert into TEAM(team_id, team_name) values (?, ?)', row)


csvReader = csv.reader(open('match.csv'))
next(csvReader)
for row in csvReader:
    cur.execute('insert into MATCH(match_id, season_year, team1, team2, battedfirst, battedsecond, venue_name, city_name, country_name, toss_winner, match_winner, toss_name, win_type, man_of_match, win_margin) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)


csvReader = csv.reader(open('player.csv'))
next(csvReader)
for row in csvReader:
    cur.execute('insert into PLAYER(player_id, player_name, dob, batting_hand, bowling_skill, country_name) values (?, ?, ?, ?, ?, ?)', row)


csvReader = csv.reader(open('player_match.csv'))
next(csvReader)
for row in csvReader:
    cur.execute('insert into PLAYER_MATCH(playermatch_key, match_id, player_id, batting_hand, bowling_skill, role_desc, team_id) values (?, ?, ?, ?, ?, ?, ?)', row)


csvReader = csv.reader(open('ball_by_ball.csv'))
next(csvReader)
for row in csvReader:
    cur.execute('insert into BALL_BY_BALL(match_id, innings_no, over_id, ball_id, striker_batting_position, runs_scored, extra_runs, out_type, striker, non_striker, bowler) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)


# cur.execute('select player_id, dob from PLAYER')
# for row in cur: #just testing
#     print(row)