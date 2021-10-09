print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission to find the treasure")

choice1 = input(
    "You're at a crossroad, which way do you want to go? Type Left or Right?\n").lower()
if choice1 == "left":
    choice2 = input(
        "You come across a river, do you swim across or find another way around? Type Swim or Another Way\n").lower()
    if choice2 == "Another Way" or "another":
        choice3 = input("Type Red, Green, Yellow, or Blue\n").lower()
        if choice3 == "Yellow":
            print("Congrats you've found the treasure")
        elif choice3 == "Red":
            print("You Fall into a pit of fire")
            print("Game Over")
        elif choice3 == "Blue":
            print("There are dozens of beasts on the otherside and they tear you apart")
            print("Game Over")
else:
    print("You are attacked by a giant fish.")
    print("Game Over")
