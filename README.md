# 🎲 Tuple Out Dice Game

## 📋 Project Overview
The **Tuple Out Dice Game** is a two-player game where players take turns rolling dice to accumulate points, aiming to reach the target score first. However, beware of "tuple out" situations where all dice show the same value, resulting in zero points for the round.

## 🕹️ Game Rules

1. **Starting the Game**:
   - Each player rolls three dice per turn.
   - The game ends when a player reaches or exceeds the target score (default: 30 points).

2. **Fixed Dice**:
   - If two dice show the same value (e.g., `4, 4, 5`), these dice are "fixed" and cannot be rerolled.
   - Only the remaining non-fixed dice can be rerolled.

3. **Tupled Out**:
   - If all three dice show the same value (e.g., `3, 3, 3`), the player "tuples out," scoring **0 points** for the round.

4. **Rerolling**:
   - Players can reroll non-fixed dice multiple times until they either decide to stop or tuple out.
   - Fixed dice remain the same during rerolls.

5. **Stopping**:
   - Players can stop rerolling at any point during their turn to lock in their current score for the round.

6. **Timeout**:
   - Players have a limited time (30 seconds) to decide whether to reroll or stop.
   - If a player fails to respond within the timeout, they forfeit their reroll and keep the current dice.

7. **Winning**:
   - The first player to reach or exceed the target score (30 points) wins the game.

## 🛠️ Program Setup and Execution
1. Make sure you have the following installed:
    - Python 3.x
    - Pandas library (`pip install pandas`)

2. Download the script: `tuple_out_main.py`.
3. Open a terminal and navigate to the script's directory.
4. Run the script with the command:
   ```bash
   python tuple_out_main.py
5. Get started following the on-screen prompts to input player names and take turns rolling dice

## ✨ Special Game Features
- **Custom Player Names**: Players can input their names at the start of the game.
- **Dynamic Rerolling**: Players can reroll non-fixed dice until they decide to stop or tuple out.
- **Score History**: Tracks each round's results using a detailed table.
- **Average Scores**: Displays the average scores of both players at the end of the game.
- **Game Statistics**: Calculates average scores per player and tracks the game history using a table.
- **Customization**: The game can be customized by modifying the game_settings dictionary in the code
    - Target Score: Adjust the winning score ('TARGET_SCORE').
    - Timeout: Change the decision timeout in seconds ('TIMEOUT').
    - Number of Dice: Modify the number of dice rolled per turn ('NUM_DICE').

## 🎉 Enjoy the Game!
Feel free to share feedback or suggest improvements. Have fun playing the Tuple Out Dice Game!

**Credits:** Nakshatra Hiray and Jahnavi Vemuri for Peer Review
