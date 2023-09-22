#list
# list = []
import random
random_integer = random.randint(1, 10) #this is 1 to and inluding 10
print(random_integer)
#0.000 - 0.99999.... not including 1
random_float = random.random() 
random_float * 5 #0.0000 - 4.9999....
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}.")
print("-----------\n")
states_of_America = ["Delaware", "California","Pennsylvania","New Jersey", "Georgia", "Connecticut"]
states_of_America.append("Massachusetts")
states_of_America.append("Maryland")
states_of_America.remove("California")
print(states_of_America)
print("-------------\n")
# exercise
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#gives the index of each name
randomIndex = random.randrange(len(names))
# print(randomIndex)
# we want to get the name of that index
randomName = names[randomIndex]
#finally we print out the phrase
print(f"{randomName} is going to buy the meal today!")
print("------------\n")
# Dr. Angela Yu notes
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#total of number in list
# print(len(names))
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")
