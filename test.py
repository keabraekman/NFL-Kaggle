import csv

print("hello world")


def score(game_id):
    with open('../nfl-big-data-bowl-2021/plays.csv') as f:
        mycsv = csv.reader(f)
        for row in mycsv:
            current_id = row[0]
            if(current_id == game_id and row[16] != '' and row[17] != ''):
                # print('row[16] = ', type(row[16]))
                game_final_row = row
        return [game_final_row[16], game_final_row[17]]



def all_game_ids():
    game_ids = []
    with open('../nfl-big-data-bowl-2021/plays.csv') as f:
        mycsv = csv.reader(f)
        for row in mycsv:
            game_ids.append(row[0])
    return game_ids


print(all_game_ids())
    