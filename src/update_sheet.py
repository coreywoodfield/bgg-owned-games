#!/usr/bin/python

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import csv
from operator import itemgetter


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client-secret.json', scope)
client = gspread.authorize(creds)

games_owned = client.open('Games')
sheet = games_owned.sheet1

people = dict(csv.reader(open('usernames.csv')))

def get_owned_games(username):
    games = requests.get('https://bgg-json.azurewebsites.net/collection/{}'.format(username)).json()
    return [game for game in games if game['owned']]

all_games = {}
for person, username in people.iteritems():
    games = get_owned_games(username)
    for game in games:
         name = game['name']
         if name in all_games:
              all_games[name]['owners'].append(person)
         else:
              game['owners'] = [person]
              rank = game['rank']
              if rank == -1:
                  game['rank'] = float('inf')
              all_games[name] = game


all_games = sorted(all_games.values(), key=itemgetter('rank'))

sheet.clear()
sheet.insert_row(['Game', 'Who has it', 'Players'])
row = 2
for game in all_games:
    sheet.insert_row([game['name'], ', '.join(game['owners']), '{}-{}'.format(game['minPlayers'],game['maxPlayers'])], row)
    row += 1

