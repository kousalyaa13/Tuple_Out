import random
import time

# Define the timeout in seconds
timeout = 30

# Re-roll feature with fixed dice logic
def reroll_decision(player_name, rolls, fixed_dice):
    """
    Handle the reroll decision for the player, with a timeout for the response.
    """
    # Get the indices of fixed dice
    fixed_indices = [index for index, roll in enumerate(rolls) if roll in fixed_dice]

    # Tell the player the current rolls and fixed dice only if the player has fixed rolls
    if fixed_dice:
        print(f"{player_name}'s current rolls are {rolls}. Fixed dice are {fixed_dice}.")
    else:
        print(f"{player_name}'s current rolls are {rolls}.")

    # Ask the player if they want to reroll, with a timeout
    print(f"\n{player_name}, you have {timeout} seconds to decide.")

    # Start the time measurement for timeout
    start_time = time.time()

    # Loop until timeout or valid input is received
    while True:
        # Check for timeout (if elapsed time exceeds the timeout limit)
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            print(f"\n{player_name} took too long to respond! No reroll allowed.")
            return rolls  # Return the original rolls if no response within the timeout

        # Ask the player if they want to reroll
        reroll_choice = input(f"\n{player_name}, would you like to reroll your dice? Enter 'yes' to reroll or 'no' to keep your current rolls: ").lower()

        # Handle invalid input
        if reroll_choice not in ['yes', 'no']:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            continue  # If invalid input, ask again

        # If the player chooses 'yes', reroll the non-fixed dice
        if reroll_choice == "yes":
            rerolled_dice = [
                random.choice(range(1, 7)) if index not in fixed_indices else rolls[index]
                for index in range(3)
            ]
            print(f"\n{player_name}'s new rolls after reroll: {rerolled_dice}")
            return rerolled_dice

        # If the player chooses 'no', return the current rolls
        print(f"\n{player_name} chose not to reroll. Rolls remain: {rolls}")
        return rolls

def roll_dice():
    """
    Simulate rolling three dice and return the results as a list.
    """
    return random.choices(range(1, 7), k=3)

# Rule: if all 3 dice rolls are the same, player has "tupled out" --> points = 0
def check_tupled_rolls(rolls, player_name):
    # Check if all three dice are the same (tuple out), score = 0
    if rolls.count(rolls[0]) == 3:
        print(f"{player_name} tupled out! All three dice are the same.")
        return 0
    return None

# Rule: if 2 dice rolls are the same, those dice are "fixed", cannot re-roll
def check_fixed_rolls(rolls):
    # Make this a tuple
    fixed_dice = tuple(roll for roll in rolls if rolls.count(roll) == 2)
    return fixed_dice

# Function for calculating score based on rolls and fixed dice
def calculate_score(rolls, fixed_dice):
    score = 0
    # Ensure that the fixed dice are also added to the score
    for roll in rolls:
        score += roll
    return score