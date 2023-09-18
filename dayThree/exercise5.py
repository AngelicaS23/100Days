#notes
"""
if condition1 & condition2 & condition3:
    do this
else:
    do this
"""

#how do we combine and check for different condition
#all in the same line
# Logical Operators
# A and B  both have to be true, if one is not true, it's false
# C or D   either can be true to work. unless both are false then it's false
# not E    reverses a condition true become false vice versa

# print("Welcome to the rollercoaster!")
# height = float(input("What is your height in cm? "))

# bill = 0 
# if height >= 120 :
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12 :
#         bill = 5
#         print("Please pay $5.")
#     elif age <= 18:
#         bill = 7
#         print("Please pay $7.") 
#     elif age >= 45 and age <= 55:  #using logical operator
#         print("It's going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Please pay $12.")
    
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill = bill + 3    #add 3$ to their bill or bill += 3 
#     print(f"Your final bill is {bill}. ")

# else: 
#     print("Sorry, you need to be tall.") 
#exercise
# You are going to write a program that tests the compatibility between two people.
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n ")
name2 = input("What is their name? \n ")
combinedName = name1 + name2
#using lower() function
combinedNameLower = combinedName.lower()
#how many times does 'true' occur in name1, name2
t_occurs = combinedNameLower.count('t')
r_occurs = combinedNameLower.count('r')
u_occurs = combinedNameLower.count('u')
e_occurs = combinedNameLower.count('e')
#add occurrence and then combine total
totalTrue = t_occurs + r_occurs + u_occurs + e_occurs

l_occurs = combinedNameLower.count('l')
o_occurs = combinedNameLower.count('o')
v_occurs = combinedNameLower.count('v')
e_occurs = combinedNameLower.count('e')
totalLove = l_occurs + o_occurs + v_occurs + e_occurs

loveScore = int(f"{totalTrue}{totalLove}")

# Love Scores
if loveScore < 10 or loveScore > 90 :
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore > 40 and loveScore < 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")

# Dr. Angela Yu Notes
combined_string = name1 + name2 #easier to combine names in one variable
lower_case_string = combined_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t + r + u + e
l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love = l + o + v + e
#can convert str to int on same line or make new variable
love_score = int(str(true)) + int(str(love))
int_score = int(love_score)# new variable for int
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
