#!/usr/bin/env python3 
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

print(players)

max_score = 50
player_scores = [0 for _ in range(players)]
#player_scores = [0]*players
print(player_scores)
