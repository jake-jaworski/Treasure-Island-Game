import sys
print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

begin = input("Ready to begin? Yes or No\n").lower()

if begin == "yes":
  print("Let's get going!")
else:
  print("Abort abort!")
  sys.exit()

road = input ("You're walking down the path and you reached a fork in the road.\nLeft or Right? ").lower()

if road == "left":
  lake = input("You've reached a lake with an island in the middle.\nWait for a boat or swim? ").lower()
  if lake == "wait" or lake == "wait for a boat":
    door = input("You waited for the boat and it took you to the island. Now you see three doors colored Blue, Red, and Yellow.\nWhich color do you pick? ").lower()
    if door == "blue":
      print("Eaten by monsters! Game over!")
    elif door == "red":
      print("You stepped into a fire. Game over!")
    elif door == "yellow":
      print("You found the treasure! You win!")
    else:
      print("Game over!")
  else:
    print("You were attacked by a gigantic fish. Game over!")
else:
    print("You fell in a dark hole. Game over!")
    

