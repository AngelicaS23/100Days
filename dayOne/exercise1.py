#ex.1
print("Day 1 - Python Print Function")
print("The function is declared like this: ")
print("print('what to print')")

#ex.2
#adding space by concatenating
print("Hello" + "Angelica") #no space
print("Hello" + " " + "Angelica") 
print("Hello " + "Angelica") 

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world)')
print("New lines can be created with a backlash and n.")

#ex.3 Input Function
# input() will get user in console 
# then print() will print the word "Hello" and the user input
print("Hello " + input("What is your name?") + "!")

# Write a program that prints the number of characters in a user's name.
name = input("What is your name? ") 
print(len(name))