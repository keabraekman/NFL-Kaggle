
# edit in here, run in terminal, save/push to git on terminal:
#1. git add .
#2. git commit -m "message"
#3. git push

# create function that returns player characteristics (height,weight,etc.) with playerid as input
# the data is in players.csv
# use score function as ex, find all chrs. and turn them into a list
# might have to convert from str to flt, etc.


import csv
# This function returns the characteristics of a player given the nfl id.
def stats(nflId):
    with open('../nfl-big-data-bowl-2021/players.csv') as f:
        mycsv = csv.reader(f)
        for row in mycsv:
            #print(row)
            playerid = row[0]
            if(playerid == nflId):
                player = row
                return [str(player[6]), str(player[1]), str(player[2]), str(player[3]),
                str(player[4]),str(player[5])]
##        return [str(row[6]), str(row[1]), str(row[2]), str(row[3]),
##                str(row[4]),str(row[5])]
##stats(2539653)



#next, create function that returns their playerid's, similar to all game ids function



def all_player_ids():
    player_ids = []
    with open('../nfl-big-data-bowl-2021/players.csv') as f:
        mycsv = csv.reader(f)
        for row in mycsv:
            if(row[0] not in player_ids):
                player_ids.append(row[0])
    return player_ids

print(all_player_ids())




