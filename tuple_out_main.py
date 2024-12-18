import random
import time

# import the helper functions
from tuple_out_helper_functions import (
    roll_dice,
    reroll_decision,
    check_tupled_rolls,
    check_fixed_rolls,
    calculate_score,
)

# handle a player's turn
def player_turn(player_name, dice_rolls, current_score):
    
    print(f"\n{player_name} is rolling the dice...")
    time.sleep(1)  # simulate a delay
    
    # roll the dice initially
    rolls = roll_dice()

    # check if player tupled out
    round_score = check_tupled_rolls(dice_rolls, player_name)
    
    if round_score is None:
        # check fixed dice and handle reroll
        fixed_dice = check_fixed_rolls(dice_rolls)
        dice_rolls = reroll_decision(player_name, dice_rolls, fixed_dice)
        
        # recheck for tupled out after reroll
        round_score = check_tupled_rolls(dice_rolls, player_name)
        
        # if still not tupled out
        if round_score is None:
            round_score = calculate_score(dice_rolls, fixed_dice)
    
    current_score += round_score
    print(f"{player_name}'s score this round: {round_score}, total score: {current_score}")
    return current_score

# get the player names
player_1 = input("Player 1, enter your name: ").strip()
player_2 = input("Player 2, enter your name: ").strip()

# initialize player scores
scores = {player_1: 0, player_2: 0}

# set target score to end the game
TARGET_SCORE = 50

# main game loop
while all(score < TARGET_SCORE for score in scores.values()):
    for player in scores:
        scores[player] = player_turn(player, roll_dice(), scores[player])

        # check if the player has reached or exceeded the target score
        if scores[player] >= TARGET_SCORE:
            print(f"\n{player} wins with {scores[player]} points!")
            break
    
    # only executed if there is no winner, avoids breaking outer loop
    else:
        continue
    break