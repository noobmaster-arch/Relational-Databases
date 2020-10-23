import sqlite3
import csv

conn=sqlite3.connect('ipl.db')
cur=conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS TEAM(
    team_id INT PRIMARY KEY,
    team_name TEXT
);''')
csvReader = csv.reader(open('team.csv'))
for row in csvReader:
    cur.execute('insert into TEAM(team_id, team_name) values (?, ?)', row)
    
cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS MATCH(
    match_id INT PRIMARY KEY, 
    season_year INT, 
    team1 INT, 
    team2 INT, 
    battedfirst INT, 
    battedsecond INT, 
    venue_name TEXT, 
    city_name TEXT, 
    country_name TEXT, 
    toss_winner INT, 
    match_winner INT, 
    toss_name TEXT, 
    win_type TEXT, 
    man_of_match INT, 
    win_margin INT
);''')
csvReader = csv.reader(open('match.csv'))
for row in csvReader:
    cur.execute('insert into MATCH(match_id, season_year, team1, team2, battedfirst, battedsecond, venue_name, city_name, country_name, toss_winner, match_winner, toss_name, win_type, man_of_match, win_margin) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)

cur.execute('select match_id, venue_name from MATCH')
for row in cur: #just testing
    print(row)