#BMI Calculator
"""
addition: +
substraction: -
multiplication: *
division: /
exponent: ** ex. 2**3 = 4*2 = 8
PEMDASLR = the order of doing the operation
print(3*3+3/3-3) = 7

"""

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# convert the result to a whole number
#bmi = wieght / height ** 2
height = input("enter your height in m: ") #string needs to convert
weight = input("enter your weight in kg: ") #string needs to convert

#creating new variables
new_weight = int(weight) #conversion to int
new_height = float(height) #converstion to float

#using the exponent operator **
bmi = new_weight / new_height ** 2 
# print(int(bmi))

#or using multiplication and PEMDAS
bmi = new_weight / (new_height * new_height)
bmi_as_int = int(bmi)
print(bmi_as_int)