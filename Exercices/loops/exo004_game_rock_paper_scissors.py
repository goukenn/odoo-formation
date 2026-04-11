# exercise: Rock - Paper - Scissors
# Write a program that allow two player to play "Rock - Paper - Scissors".
# each player enter their name, and then the game begin
# each player takes their turn,n and the program determines the winner of the round and awards 1 point.
# - rock beats scissors
# - scissors beats paper
# - paper beats rock
# the first player to reach 3 points wins. A tie scrores no points
from random import randint 

player1 = { "name": '', "score": 0}
player2 = { "name": '', "score": 0}

 
player1["name"] = input('player 1 name ')
player2["name"] = input('player 2 name ')

print('Game start ....')

v_list = ['Rock','Paper','Scissors']

while True:
    p = randint(0,2) # player one play
    o = randint(0,2) # player two play
    o1 = 0
    o2 = 0
    if p == o:
        continue
    else:
        if v_list[p] =='Rock':
            if v_list[o]=='Paper':
                o2 = 1
            else:
                o1 = 1
        elif v_list[p] =='Paper':
            if v_list[o]=='Scissors':
                o2 = 1
            else:
                o1 = 1
        else:
            if v_list[o]=='Rock':
                o2 = 1
            else:
                o1 = 1
    player1['score'] = player1['score'] + o1
    player2['score'] = player2['score'] + o2
    print(f"coup : {v_list[p]} vs {v_list[o]}")
    
    if player1['score'] == 3 or player2['score'] == 3:
        break

winner = player1 if player1['score'] == 3 else player2
if player2 is winner:
    victory = 'flawless vitory' if not player1['score'] else '' 
    print(f'player 2 : {winner['name']} win!!!', victory)
else: 
    victory = ' flawless vitory' if not player2['score'] else '' 
    print(f'player 1: {winner['name']} win!!!', victory)


