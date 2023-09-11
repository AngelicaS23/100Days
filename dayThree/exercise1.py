#control flow with if/else and conditional operators
# conditional statment
# if condition:
#     do this
# else:
#     do this

#practice
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:  #can include 120 by adding =
    print("You can ride the rollercoaster!")  #this line of code lives in if statment
else:
    print("Sorry, you have to grow taller.")  #this code of block lives in else

print("----------\n")
#comparison Operators
# >, <, <=, >=, ==, !=

#if its 0 its True, if its 1 its false
print(54%2)  # 0
print(4%2)  # 0
print(12%2)  #0
print(33%2)  #1
print(25%2)  #1

print("----------\n")

#exercise 1
# Write a program that works out whether if a given number is an odd or even number.
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number")

