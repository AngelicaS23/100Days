#if/elif/else
""" 
if condition1:
    do A
elif condition2: # only of these things will be carry out
    do B
else:
    do C
"""
# multiple if statements in succession
"""
if condition1:  
    do A
if condition2:
    do B
if condition3:
    do C 
"""
#example:
print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm? "))

bill = 0 
if height >= 120 :
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12 :
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.") 
    else:
        bill = 12
        print("Please pay $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill = bill + 3    #add 3$ to their bill or bill += 3 
    print(f"Your final bill is {bill}. ")

else: 
    print("Sorry, you need to be tall.")

print("\n")
# Your first job is to build an automatic pizza order program.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill = 15
    # print("pay 15")
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    # print("pay 20")
    if add_pepperoni == "Y":
        bill += 3 
elif size == "L":
    bill = 25
    # print("pay 25")
    if add_pepperoni == "Y":
        bill += 3 
if extra_cheese == "Y":
    bill += 1
print(f"Your finall bill is {bill}. ")

#Dr. Angela Yu Notes
bill = 0
#size of pizza
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:           #or use elif and omit else
    bill += 25
#addition to pizza 
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")
