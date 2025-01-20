Based on [Emily Bache](https://github.com/emilybache) *"The Coding Dojo Handbook"* through [dfleta's Bowling Game Kata](https://github.com/dfleta/bowling-game-kata-automata) for *Cross-platform App Developement 2024-2026* (IES TEIS).

----------------------
 # Bowling Score Calculator
 This program takes a basic annotation of a full bowling game and returns the already calculated final score. It takes an only argument of the fast annotation of a game in a string form, in which:

 - **-** is a missed roll.
 - **/** is a spare.
 - **X** is a strike. 

 The program lacks any formatter or data checker, so it will always expect a string of length 20 or more (only up to 23, the maximum rolls in bowling, have been tested). It uses a class contained in [scoreCalculator.py](https://github.com/MMSS99/Bowling-Game-py/blob/main/src/scoreCalculator.py) with a single public method `calculateScore` that uses private methods to pass to the user the summed final score of the match. 