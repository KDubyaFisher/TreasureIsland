print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

user_choice1 = input(f'You awaken on a beach. Which way do you go? Type "left" or "right"').lower()
if user_choice1 == "left":
    user_choice2 = input(f"You see an island in the distance and a boat on it's way to shore."
                         f" Do you attempt to swim to it or wait for the boat?").lower()
    if user_choice2 == "wait":
        user_choice3 = input(f'You arrive at the island unharmed and see a building with three doors. '
                             f'Which door do you choose? Type "blue", "yellow", or "red"').lower()
        if user_choice3 == "yellow":
            print("You Win!!!")
        elif user_choice3 == "red":
            print("You were burned alive by the flames of hell. OUCH! Cwispy! GAME OVER! YOU LOSE!")
        elif user_choice3 == "blue":
            print("You were eaten alive by rabid beasts! Yumm! GAME OVER! YOU LOSE!")
        else:
            print("What the hell?! You don't know how to follow instructions so GAME OVER! YOU LOSER!")
    else:
        print("You were eaten by a school of vicious trout. GAME OVER! YOU LOSE!")
else:
    print("You fell off the world into the infinite void... Good bye! GAME OVER! YOU LOSE!")


