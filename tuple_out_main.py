import random
import time
import pandas as pd

TIMEOUT = 30  # Timeout for player decision
TARGET_SCORE = 30  # Target score to win the game

def roll_dice():
    """
    simulate rolling three dice and return the results as a list.
    """
    return random.choices(range(1, 7), k=3)

def check_tupled_rolls(rolls, player_name):
    """
    check if all three dice are the same (tuple out).
    """
    if rolls.count(rolls[0]) == 3:
        print(f"{player_name} tupled out! All three dice are the same.")
        return 0  # points = 0 if tupled out
    return None

def check_fixed_rolls(rolls):
    """
    check for fixed dice (two dice of the same value).
    """
    fixed_dice = tuple(roll for roll in rolls if rolls.count(roll) == 2)
    return fixed_dice

def calculate_score(rolls, fixed_dice):
    """
    calculate the score for the player based on the rolls and fixed dice.
    """
    return sum(rolls)  # Add all rolls together for the score

# Player Interaction Functions
def reroll_decision(player_name, rolls, fixed_dice):
    """
    handle the reroll decision for the player, with a timeout for the response.
    """
    fixed_indices = [index for index, roll in enumerate(rolls) if roll in fixed_dice]

    # Inform player about their current rolls and fixed dice
    if fixed_dice:
        print(f"{player_name}'s current rolls are {rolls}. Fixed dice are {fixed_dice}.")
    else:
        print(f"{player_name}'s current rolls are {rolls}.")
    
    print(f"\n{player_name}, you have {TIMEOUT} seconds to decide.")

    start_time = time.time()

    # wait for player's decision, with timeout
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > TIMEOUT:
            print(f"\n{player_name} took too long to respond! No reroll allowed.")
            return rolls  # Return original rolls if timeout occurs

        reroll_choice = input(f"\n{player_name}, would you like to reroll your dice? Enter 'yes' to reroll or 'no' to keep your current rolls: ").lower()
        if reroll_choice not in ['yes', 'no']:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            continue  # Ask again for valid input

        if reroll_choice == "yes":
            rerolled_dice = [
                random.choice(range(1, 7)) if index not in fixed_indices else rolls[index]
                for index in range(3)
            ]
            print(f"\n{player_name}'s new rolls after reroll: {rerolled_dice}")
            return rerolled_dice

        print(f"\n{player_name} chose not to reroll. Rolls remain: {rolls}")
        return rolls

# main game loop functions
def player_turn(player_name, current_score):
    """
    handle a player's turn, including dice rolls, rerolls, and score calculation.
    """
    print(f"\n{player_name} is rolling the dice...")
    time.sleep(1)  # simulate a delay

    rolls = roll_dice()  # roll the dice
    round_score = check_tupled_rolls(rolls, player_name)

    if round_score is None:
        fixed_dice = check_fixed_rolls(rolls)
        rolls = reroll_decision(player_name, rolls, fixed_dice)

        round_score = check_tupled_rolls(rolls, player_name)  # recheck after reroll
        if round_score is None:
            round_score = calculate_score(rolls, fixed_dice)  # calculate score if not tupled out

    current_score += round_score  # update total score
    print(f"{player_name}'s score this round: {round_score}, total score: {current_score}")
    return current_score

# initialize game and player setup
def setup_game():
    """
    Get the player names and initialize the game state.
    """
    player_1 = input("Player 1, enter your name: ").strip()
    player_2 = input("Player 2, enter your name: ").strip()
    scores = {player_1: 0, player_2: 0}
    return player_1, player_2, scores

# game statistics using pandas
def calculate_statistics(score_history, player_1, player_2):
    """
    calculate and display the average scores for each player.
    """
    average_scores = score_history[[player_1, player_2]].mean(axis=0)

    print("\nAverage Scores (per player):")
    print(average_scores)

# executing the main game
def play_game():
    player_1, player_2, scores = setup_game()

    # create DataFrame to track scores over multiple rounds
    columns = ['Round', player_1, player_2, 'Total ' + player_1, 'Total ' + player_2]
    score_history = pd.DataFrame(columns=columns)

    round_number = 1

    # main game loop
    while all(score < TARGET_SCORE for score in scores.values()):
        round_scores = {'Round': round_number}
        
        for player in scores:
            scores[player] = player_turn(player, scores[player])
            round_scores[player] = scores[player]
            round_scores['Total ' + player] = scores[player]

        # append round scores to the score history DataFrame
        score_history = pd.concat([score_history, pd.DataFrame([round_scores])], ignore_index=True)

        # check if a player has reached the target score
        for player in scores:
            if scores[player] >= TARGET_SCORE:
                print(f"\n{player} wins with {scores[player]} points!")
                break
        else:
            round_number += 1
            continue  # no winner yet, continue the game loop
        break  # exit the loop if there is a winner

    # display final results
    print("\nFinal Scores:")
    print(scores)

    print("\nScore History:")
    print(score_history)

    # calculate and display average scores
    calculate_statistics(score_history, player_1, player_2)

# run the game
if __name__ == "__main__":
    play_game()