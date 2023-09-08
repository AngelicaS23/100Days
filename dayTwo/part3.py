#number manipulation and F string 
print(8/3) #gives us 2.6666666 
print(int(8/3)) # gives us 2 but we want to round it
print(round(8/3)) #use round() built in function = 3
print(round(8/3, 2)) #rounding it to 2 decimal places = 2.67
print(8//3) #two // gives us 2 and we don't have to convert to int()
result = 4/2
result /= 2
print(result) # 1?

# ex: 
score = 0 #int
heigth = 1.8 #float
inWinning = True #boolean
print("your score is " + str(score)) #had to convert score into str() to match data type
#f-string does all the conversion
print(f"your score is { score}, your heigth is {heigth}, you are winning is {inWinning}")

#Your Life in Weeks Exercise

# Create a program using maths and f-Strings that tells us how many 
# days, weeks, months we have left if we live until 90 years old
# Output : You have x days, y weeks, and z months left.

age = input("What is your current age? ")

originalYears = 90 
daysYear = 365 
weeksYear = 52
monthsYear = 12

yearLeft = originalYears - int(age) # subtract 90 with user input for how many years left
#multiply yearLeft with days, weeks, month a year to get how much each is left
daysLeft = yearLeft * daysYear 
weeksLeft = yearLeft * weeksYear
monthLeft = yearLeft * monthsYear

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthLeft} months left.")

# or this works too and its easier to read
age_as_int = int(age) #convert before subtracting 90 to user input 
yearsRemaining = 90 - age_as_int
daysRemaining = yearsRemaining * 365
weeksRemaining = yearsRemaining * 52
monthsRemaining = yearsRemaining * 12
message = f"You have {daysRemaining} days, {weeksRemaining} weeks, and {monthsRemaining} months left."
print(message)
