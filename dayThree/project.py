#Treasure Island

# print('''
#                         _.-'_:-'||
#                     _.-'_.-::::'||
#                _.-:'_.-::::::'  ||
#              .'`-.-:::::::'     ||
#             /.'`;|:::::::'      ||_
#            ||   ||::::::'     _.;._'-._
#            ||   ||:::::'  _.-!oo @.!-._'-.
#            \'.  ||:::::.-!()oo @!()@.-'_.|
#             '.'-;|:.-'.&$@.& ()$%-'o.'\U||
#               `>'-.!@%()@'@_%-'_.-o _.|'||
#                ||-._'-.@.-'_.-' _.-o  |'||
#                ||=[ '-._.-\U/.-'    o |'||
#                || '-.]=|| |'|      o  |'||
#                ||      || |'|        _| ';
#                ||      || |'|    _.-'_.-'
#                |'-._   || |'|_.-'_.-'
#             jgs '-._'-.|| |' `_.-'
#                     '-.||_/.-'
# ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

question1 = input("You're at a cross road. Where do you want to go? Type 'Left' or 'Right'\n")
question1_lower = question1.lower() 

if question1_lower == 'left':
    question2 = input("To cross the lake, do you swim or wait for a boat?\n")
    question2_lower = question2.lower()
    if question2_lower == 'wait':
        question3 = input("Which door do you open? Red, Blue, or Yellow?\n")
        question3_lower = question3.lower()
        if question3_lower == 'yellow':
            print("You Win!")  
        elif question3_lower == 'red':
            print("Burned by fire. Game Over.")
        elif question3_lower == 'blue' :
            print("Eaten by beasts. Game Over.")    
        else:
            print("Game Over!")
    else: 
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")

# Dr. Angela Yu Notes
choice1 = input("You're at a cross road. Where do you want to go? Type 'Left' or 'Right' ").lower()
if choice1 == "left":
    #game will continue
    choice2 = input("You've come to a lake. There's an island in the middle of th lake. Do you 'Wait' or 'Swim'?").lower()
    if choice2 == "wait":
        #game will continue
        choice3 = input("you arrived at the island. There is a house with 3 doors. which one do you choose: One red, Two blue, or Three Yellow?").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over")
    else:
        print("you got attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")
