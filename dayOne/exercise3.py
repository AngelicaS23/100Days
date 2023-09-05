#Input Function
# input() will get user in console 
# then print() will print the word "Hello" and the user input
print("Hello " + input("What is your name?") + "!")

# Write a program that prints the number of characters in a user's name.
name = input("What is your name? ") #can assign input into a variable 
print(len(name)) #the variable is used when printing 

#or, but not as clean as the first option
print( len( input("What is your name?"))) # fill it all in one line for same result