###############################
# MIDTERM - ANA1001
# Nayane Ferreira da Silva (A00302986)
###############################

import random

# Rooms and their descriptions
rooms = {
    "Gryffindor common room":"You are in the Gryffindor common room. It feels warm and cozy, with a crackling fireplace and plush armchairs.",
    "Slytherin common room":"You are in the Slytherin common room. It's dimly lit and decorated with green and silver accents.",
    "Ravenclaw common room":"You are in the Ravenclaw common room. The walls are adorned with bookshelves and the ceiling reflects the night sky.",
    "Hufflepuff common room":"You are in the Hufflepuff common room. It's bright and cheerful, with sunlight streaming in through the windows.",
    "Dumbledore's office":"You are in Dumbledore's office. The room is filled with curious objects and magical artifacts."
}

# Interactions with characters
characters = {
    "Dumbledore": "Hi Harry, I have an important task for you, but to earn it, you need to guess the number I am thinking. Pick a number between 0 and 5.",
    "Malfoy": "What are you doing here Potter? This is not your place! I challenge you to a duel."
}

# Player attributes
player = {
    "health": 100,
    "gold": 0,
    "items": 0,
    "horcruxes": []
}

#Setting the initial stage: Starting at Gryffindor commom room
print("Hello Harry Potter! \nWelcome to Hogwarts! \nSince you have been chosen for Gryffindor, you must start the game in your house! You must find the Horcruxes and destroy them, otherwise, you will be killed by Voldemort!\nGood luck!")
current_room = "Gryffindor common room"

#User input
user_input = 0

# Game loop
while True:

# Check for special actions in each room
    if user_input == "0" or current_room == "Gryffindor common room":
        print("\n"+rooms[current_room])
        print("Press [1] to go to Slytherin common room")
        print("Press [2] to go visit Dumbledore")
        print("Press [3] to go to Hufflepuff common room")
        print("Press [4] look for a Horcrux")
        print("Press [5] to collect an item")
    #User input
        user_input = input ("Enter your choice: ")

    #Continue loop based on user choice
    #Option 1: Slytherin Common room
    if user_input == "1" or current_room == "Slytherin common room":
        current_room = "Slytherin common room"
        print("\n"+ rooms[current_room])
        print("You encounter Malfoy: " + characters["Malfoy"])
        user_input = input("Press [6] to accept the challenge or [7] to decline: ")
        if user_input == "6":
            print("\n" + "You bravely accept the challenge and defeat Malfoy. He gives you a reward.")
            player["gold"] += 50
            print(f'Congratulation. You earned 50 in gold. Your current amount: {player["gold"]}.')
        else:
            print("\n"+"You decline the challenge and avoid a confrontation. You loose 50 of health")
            player["health"] -= 50
            print(f'Your current health is: {player["health"]}.')
            if player["health"] < 1:
                print ("You have zero of health. You have been defeated and is dead. Game Over.")
                break

        current_room = "Dumbledore's office"

    #Option 2:Dumbledore's office
    if user_input == "2" or current_room == "Dumbledore's office":
        current_room = "Dumbledore's office"
        print("\n"+rooms[current_room])
        if "Marvolo Gaunt's Ring" in player["horcruxes"]:
            print ("I see you still have the horcrux I gave you. It must be destroyed.")
        else:
            print(characters["Dumbledore"])
            guess = int(input("What is your guess? "))
            if guess == random.randint(0, 5):
                print("You guessed right! Receive the Marvolo Gaunt's Ring Horcrux that must be destroyed.")
                player["horcruxes"].append("Marvolo Gaunt's Ring")
                print(f'You are in possession of the following Horcruxes: {player["horcruxes"]}.')
            else:
                print("\n"+"Sorry, Harry! You guessed wrong. I still cannot trust you. Better luck the next time.")
    # User will need to choose the next room.
        print("\nPress [1] to go to Slytherin common room")
        print("Press [8] to go to Ravenclaw common room")
        user_input = input ("Enter your choice: ")

    #Option 8: Ravenclaw common room
    if user_input == "8" or current_room == "Ravenclaw common room":
        current_room = "Ravenclaw common room"
        print("\n"+rooms[current_room])
        if "Rowena Ravenclaw's Diadem" in player["horcruxes"]:
            print ("\n"+"Since you already have the Diadem, we can give you an item to destroy it.")
            player["items"] += 1
            print(f'You are in possession of {player["items"]} item(s) to destroy Horcruxes.')
        else:
            print("\n"+"You found a Horcrux - Rowena Ravenclaw's Diadem. Good job.")
            player["horcruxes"].append("Rowena Ravenclaw's Diadem")
            print(f'You are in possession of the following Horcruxes: {player["horcruxes"]}.')
        current_room = "Hufflepuff common room"

    #Option 3: Hufflepuff common room
    if user_input == "3" or current_room == "Hufflepuff common room":
        current_room = "Hufflepuff common room"
        print("\n"+rooms[current_room])
        if "The Hufflepuff's Cup" in player["horcruxes"]:
            print("Since you haven't destroyed The Hufflepuff's Cup yet. You lose all your gold.")
            player["gold"] = 0
            print(f'You have {player["gold"]} of gold.')
        else:
            print("You chose Hufflepuff common room and found a Horcrux: The Hufflepuff's Cup")
            player["horcruxes"].append("The Hufflepuff's Cup")
            print(f'You are in possession of the following Horcruxes: {player["horcruxes"]}.')
        current_room = "Gryffindor common room"

    #Option 4: Go find a Horcrux
    if user_input == "4":
        print("\n"+"You chose to look for a Horcrux. However, it's never that easy. Voldemort used Avada Kedavra on you. Game over.")
        break

    #Option 5: Go find an item to destroy a Horcrux
    if user_input == "5":
        print("\n"+"You collected an item to destroy the Horcruxes")
        player["items"] += 1
        print(f'You are in possession of {player["items"]} item(s) to destroy Horcruxes.')
        current_room = "Gryffindor common room"

    #Check for winning conditions
    if len(player["horcruxes"]) > 0:
        if len(player["horcruxes"]) < (player["items"]):
            print("\n"+"Congratulations! You found a Horcrux and destroyed it. You win!")
            break
        elif len(player["horcruxes"]) > (player["items"]):
            if player["health"] > 10:
                print ("\n"+"Your health is being compromised - Lose 10 of health.")
                player["health"] -= 10
                print(f'Your current health is {player["health"]}. If you reach zero, it is game over!')
            else:
                print("\n"+"You have a Horcrux and no item to destroy it. You have been cursed! Game over.")
                break





