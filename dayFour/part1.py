#random module. can make own random module
import random
# random_integer = random.randint(1, 10) #this is 1 to and inluding 10
# print(random_integer)
# #0.000 - 0.99999.... not including 1
# random_float = random.random() 
# random_float * 5 #0.0000 - 4.9999....
# print(random_float)

# love_score = random.randint(1,100)
# print(f"Your love score is {love_score}.")

# exercise: Heads or Tails
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
random_int = random.randint(0,1)

if random_int == 1:
    print("Heads")
else:
    print("Tails")

# Notes from Dr. Angela Yu
'''
import random
random_side = random.randint(1,0)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
'''
