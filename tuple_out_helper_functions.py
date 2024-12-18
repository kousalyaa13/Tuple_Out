import random
# added features:
# if the user spends too much time on an answer they don't get to reroll, show a counter
# when doing the roll use the time function to make it seem like it is taking some time to roll
# need to add tests for all the functions
# comment out the tests and add docstrings
# add pandas, seaborn, and/or time, 5 points for each feature, max 10 points

# store randomly rolled dice values in lists for each player
# create a function instead of manual player rolls
def roll_dice():
    return random.choices(range(1, 7), k=3)

# re-roll feature with fixed dice logic
def reroll_decision(player_name, rolls, fixed_dice):
    # get the indices of fixed dice
    fixed_indices = []
    for index, roll in enumerate(rolls):
        if roll in fixed_dice:
            fixed_indices.append(index)
    
    # tell the player the current rolls and fixed dice only if the player has fixed rolls
    if fixed_dice:
        print(f"{player_name}'s current rolls are {rolls}. Fixed dice are {fixed_dice}.")
    else:
        print(f"{player_name}'s current rolls are {rolls}.")


    # ask the player if they want to reroll
    reroll_choice = input(f"\n{player_name}, would you like to reroll your dice? Enter 'yes' to reroll or 'no' to keep your current rolls: ").lower()
    
    # handle invalid input
    while reroll_choice not in ['yes', 'no']:
        reroll_choice = input("Invalid choice. Please enter 'yes' or 'no': ").lower()

    if reroll_choice == "yes":
        # reroll only the non-fixed dice
        rerolled_dice = [
            random.choice(range(1, 7)) if index not in fixed_indices else rolls[index]
            for index in range(3)
        ]
        
        print(f"\n{player_name}'s new rolls after reroll: {rerolled_dice}")
        return rerolled_dice

    # if the player doesn't want to re-roll, return the same rolls
    print(f"\n{player_name} chose not to reroll. Rolls remain: {rolls}")
    return rolls

# rule: if all 3 dice rolls are the same, player has "tupled out" --> points = 0
def check_tupled_rolls(rolls, player_name):
    # check if all three dice are the same (tuple out), score = 0
    if rolls.count(rolls[0]) == 3:
        print(f"{player_name} tupled out! All three dice are the same.")
        return 0
    return None

# rule: if 2 dice rolls are the same, those dice are "fixed", cannot re-roll
def check_fixed_rolls(rolls):
    # make this a tuple
    fixed_dice = tuple(roll for roll in rolls if rolls.count(roll) == 2)
    return fixed_dice

# function for calculating score based on rolls and fixed dice
def calculate_score(rolls, fixed_dice):
    score = 0
    # ensure that the fixed dice are also added to the score
    for roll in rolls:
        # add all dice rolls to score, including fixed ones
        score += roll
    return score

# handle a player's turn with the stop feature added
def player_turn(player_name, score):
    print(f"\n{player_name} is taking their turn...")
    rolls = roll_dice()

    while True:
        # check if tupled out
        round_score = check_tupled_rolls(rolls, player_name)
        if round_score == 0:
            print(f"{player_name}'s score this round: 0 (tupled out).")
            return score

        # display current rolls and fixed dice if there are fixed dice using a tuple
        fixed_dice = check_fixed_rolls(rolls)
        if fixed_dice:
            print(f"Current rolls: {rolls}, Fixed dice: {fixed_dice}")
        else:
            print(f"Current rolls: {rolls}")


        # ask the player if they want to stop or continue
        stop_choice = input(f"{player_name}, would you like to 'stop' and keep your score, or 'reroll'? ").lower()

        # handle invalid input
        while stop_choice not in ['stop', 'reroll']:
            stop_choice = input("Invalid choice. Please enter 'stop' or 'reroll': ").lower()

        if stop_choice == "stop":
            # calculate and add the round's score
            round_score = calculate_score(rolls, fixed_dice)
            score += round_score
            print(f"{player_name}'s score this round: {round_score}, Total score: {score}")
            return score
        else:
            # reroll non-fixed dice
            rolls = reroll_decision(player_name, rolls, fixed_dice)