import sqlite3
import csv

conn=sqlite3.connect('ipl.db')
cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS TEAM(
    team_id INT PRIMARY KEY,
    team_name TEXT
);''')


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

