#day 2 project: Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
amountPoeple = int(input("How many people to split the bill? "))
#to get percent divide by 100
tipPercentage = (tip / 100)  # .12
#multiply 150 with .12
newTip =  bill * tipPercentage # 18
#add 150 and 18 divided by 5
total = (bill + newTip) / amountPoeple

message = "Each person should pay: "
#formating the result to 2 decimal places
print(message + '${:.2f}'.format(round(total, 2)))

#notes from Dr. Angela Yu
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill  #or bill*(1+tip/100) 
bill_per_person = bill_with_tip / people
#can use same variable for two things that will be together?
finalAmount = round(bill_per_person, 2)
finalAmount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${finalAmount}")
