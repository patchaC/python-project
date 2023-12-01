import random
from random import sample
import pandas as pd

weapon = ['Quit','Rock','Paper','Scissors']

print("Hello fighter! Choose your weapon!")

def rps() :
    sum_score = {
    "win" : 0,
    "lose" : 0,
    "tie" : 0 }

    while True:
        player = input("   Rock[1] Paper[2] Scissors[3] Exit[0]: ")
        player = int(player)
        if player == 0:
            print("Good Bye :)")
            break
        bot = sample([1, 2, 3 ], k=1)
        player_move = weapon[player]
        bot_move = weapon[bot[0]]
        print(f" {bot_move} vs {player_move} (yours)")

        if player_move == bot_move :
               print("---- Tie! Play Again ----\n" )
               sum_score['tie'] += 1
        elif ( (player_move == 'Rock' and bot_move == 'Paper') or
    	     (player_move == 'Paper' and bot_move == 'Scissors') or
             (player_move == 'Scissors' and bot_move == 'Rock') ):
              print("---- You Lose T T ----\n")
              sum_score['lose'] += 1
        else :
            print("---- You Win!! ----\n")
            sum_score['win'] += 1

        print(f"Win: {sum_score['win']} ")
        print(f"Loss: {sum_score['lose']} ")
        print(f"Tie: {sum_score['tie']}\n ")

rps()
