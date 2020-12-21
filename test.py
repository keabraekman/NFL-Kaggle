import csv

print("hello world")

# This function returns the score of a game given the game id
def score(game_id):
    with open('../nfl-big-data-bowl-2021/plays.csv') as f:
        mycsv = csv.reader(f)
        for row in mycsv:
            current_id = row[0]
            if(current_id == game_id and row[16] != '' and row[17] != ''):
                # print('row[16] = ', type(row[16]))
                game_final_row = row
        return [int(game_final_row[16]), int(game_final_row[17])]



def all_game_ids():
    game_ids = []
    with open('../nfl-big-data-bowl-2021/plays.csv') as f:
        mycsv = csv.reader(f)
        for row in mycsv:
            if(row[0] not in game_ids):
                game_ids.append(row[0])
    return game_ids

print(all_game_ids())

