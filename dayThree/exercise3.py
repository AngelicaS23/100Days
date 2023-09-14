# day 3.3 Leap year Exercise
# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February.
""" 
This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 

**except** every year that is evenly divisible by 100 

**unless** the year is also evenly divisible by 400
"""

year = int(input("Which year do you want to check? "))
isLeapYear = False  #created variable for bool: default false
if year % 4 == 0:   
    isLeapYear = True
    if year % 100 == 0:
        isLeapYear = False
        if year % 400 == 0:
            isLeapYear = True

if isLeapYear:
    print("Leap year.")
else:
    print("Not leap year.")

#notes by Dr. Angela Yu, folling the flow chart
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year.")
    else:
       print("leap year.")
else: 
    print('Not a leap year.')
