#nested if statements and elif statement

# if condition:  
#   if another condition:  inorder for this to happen, the first one has to be true
#       do this
#     else:   the first condition has to be true the 2nd condition has to be false?
#       do this
# else:  
#   do this

#example:
# print("Welcome to the rollercoaster!")
# height = float(input("What is your height in cm? "))

# if height >= 120 :
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12 :
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.") 
#     else:
#         print("Please pay $12.")
# else: 
#     print("Sorry, you need to be tall.")
# print("--------------\n")

""" 
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
"""
height = float(input("enter your height in m: ")) #1.75, 1.52
weight = float(input("enter your weight in kg: ")) #85, 68.94

#using the exponent operator **
bmi = round(weight / height ** 2)
print(bmi)

#conditional statements
if bmi >= 18.5:
    if bmi <= 25 :
        print(f"Your bmi is {bmi}, you have a normal weight.")
    elif bmi <= 30:
        print(f"Your bmi is {bmi}, you are slightly overweight.")
    elif bmi <= 35 :
        print(f"Your bmi is {bmi}, you are obese.")
    else:
        print(f"Your bmi is {bmi}, you are clinically obese.")
else:
    print(f"Your bmi is {bmi}, you are underweight.")

# Notes from Dr. Angela Yu
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:    
    print(f"Your bmi is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:    
    print(f"Your bmi is {bmi}, you are clinically obese.")
