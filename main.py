# This project is a mini-game based on chance. Two players at any one time. Each player is aiming to get to a score of 100. The first to do so wins.
# Each player decides how many times they want to roll the dice. Each time it lands on a number, that number is added to their total score.
# However, if the dice lands on 1, then the total points from that roll are removed from the players overall score.

# For example:  if a player is on 50 points, they roll 4 times per turn and the roll is 5,5,7,3 - The player remains on 70 points.
#               if a player is on 50 points, they roll 4 times per turn and the roll is 3,5,1,6 - The player remains on 50 points because 1 was rolled.

import random
def roll(player,final_score):
    roll_score=0
    rolls = int(input(f"{player},how many rolls would you like? "))

    for i in range(rolls):
        n = random.randint(1,6)
        if n==1:
            roll_score=0
            break
        roll_score += n
    return final_score+roll_score


p1_final_score = 0
p2_final_score = 0

p1_name = input("What is the name of player 1? ")
p2_name = input("What is the name of player 12? ")

# if either player score over 100, game over /// players take turns
while True:
        p1_final_score = roll(p1_name,p1_final_score)
        if p1_final_score > 100:
            break

        p2_final_score = roll(p2_name, p2_final_score)
        if p2_final_score > 100:
            break

print(f"{p1_name} final score is {p1_final_score}\n"
      f"{p2_name} final score is {p2_final_score}")