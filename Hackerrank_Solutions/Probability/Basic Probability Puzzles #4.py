
from fractions import Fraction

# Bags
bag1_red, bag1_black = 4, 5
bag2_red, bag2_black = 3, 7

# Total possible outcomes: choose 1 from bag1 and 2 from bag2
total_outcomes = (bag1_red + bag1_black) * (bag2_red + bag2_black) * (bag2_red + bag2_black - 1) // 2


# Count favorable outcomes (1 red, 2 black)
favorable_outcomes = 0

# Case 1: Red from bag1, Black and Black from bag2
favorable_outcomes += bag1_red * (bag2_black * (bag2_black - 1) // 2)

# Case 2: Black from bag1, Red and Black from bag2
favorable_outcomes += bag1_black * (bag2_red * bag2_black)

print(Fraction(favorable_outcomes, total_outcomes))