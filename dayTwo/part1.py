#primative Data Types

"""print("124" + "12")

mystery = 712_43.23
print(type(mystery))
print(mystery)

street_name = "Abbey Road"
print(street_name[4] + street_name[7])
"""

# len(234)

# num_char = len(input("What is your name?"))
# print(type(num_char))

# new_num_char = str(num_char)
# print("your name has " + new_num_char + " characters.")

# a = str(123)
# print(type(a))
# print(70 + float("100.5"))
# print(str(70) + str(100.1))

# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digits_number = input("Type a two digit number: ")
first_digits = two_digits_number[0]
second_digits = two_digits_number[1]
print(int(first_digits) + int(second_digits))
