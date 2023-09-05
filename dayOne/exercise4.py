# #variables

name = "Jack" 
print(name) #name holds Jack
name = "Angela"
print(name)

name = input("What is your name?") # assigned input () to a variable: name
length = len(name) #another variable: lenght for len()
print(length) #user has to add a name for it to get the len() of the name

# Write a program that switches the values stored in the variables a:3 and b:5.
a = input("a: ")
b = input("b: ")

temp = a #created a temp to store value of a
a = b # moved value of b to varialbe a
b = temp # the new value of b is the stored valua of a in temp

print("a: " + a)
print("b: " + b)


