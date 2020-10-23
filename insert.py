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


cur.execute('select team1, city_name from MATCH')
for row in cur: #just testing
    print(row)