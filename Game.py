import time
import random

# i tried to test my code with pycodestyle and everything is fine but it wont stop telling
# line is too long im sick of it >:(

characters = ["Old Owl", "Guardian of the forest", "Great Elf", "Fairy", "Ork"]
magical_weapon = ["sword", "potion", "wand", "Dagger"]
food_list = ["Meat", "Fruits", "Eggs", "Rare herbs"]
jewels_list = ["Magic ring", "Pearl nicklace", "Water magic bracelet"]

weapon = random.choice(magical_weapon)
helper = random.choice(characters)
food = random.choice(food_list)
jewel = random.choice(jewels_list)
cash = ("Cash:", random.randint(1, 1000000))

score = 1
player_inventory = []
user_input = 0


# User input function
def ui():
    global user_input
    user_input = input("Enter 1 or 2 based on your choice: ")


def get_choice(message, valid_inputs):
    choice = input(message)
    while choice not in valid_inputs:
        choice = input("Please enter a valid input from: " + str(valid_inputs) + "> ")
    return choice


# play again to restart game variable
def play_again():
    while True:
        response = input("Play again? (yes or no)")
        if response.lower() == "yes":
            global score
            global player_inventory
            global weapon
            global helper
            score = 1
            player_inventory = []
            weapon = random.choice(magical_weapon)
            helper = random.choice(characters)
            start_game()
        elif response.lower() == "no":
            print("Thank you for playing!")
        else:
            print("Invalid input.")


# pause function but when you have a variable at the text or end
def printpp(t, h, p):
    print(t, h)
    time.sleep(p)


# pause but no variables
def printp(t, p):
    print(t)
    time.sleep(p)


# pause with variable in the middle of the text
def printppp(t, h, i, p):
    print(t, h, i)
    time.sleep(p)


# function to start game
def start_game():
    printp("Welcome to the Magical Forest Adventure!", 2)
    print("")
    print("Note: You get a score based on your choices... be careful")
    printp("", 2)
    printp("You wake up at a mysterious forest entrance with two paths.", 3)
    print("1. Take the left path which is overgrown and looks dangerous")
    print("2. Take the right path which is lit and looks pretty")

    choice = get_choice("Enter 1 or 2 based on your choice: ", ["1", "2"])
    if choice == "1":
        left()
    elif choice == "2":
        right()


def left():
    global score
    score -= 1
    print("score:", score)
    printp(
        "You choose left. Trees thicken, light dims, and you hear rustling in the bushes.",
        3,
    )
    print("AHH!!")
    printppp(
        "Suddenly, you scream and the",
        helper,
        "attacks you, looking at you with curiosty",
        2,
    )
    printpp(
        helper,
        "A traveler? It's rare to see humans here. What brings you?",
        2,
    )
    print(
        "1.Tell the",
        helper,
        "about your quest for adventure, unsure of their intentions.",
    )
    print("2. Keep your mission a secret and ask the", helper, "for guidance.")
    choice = get_choice("Enter 1 or 2 based on your choice: ", ["1", "2"])
    if choice == "1":
        tell()
    elif choice == "2":
        keep()


def right():
    global score
    score += 2
    print("score:", score)
    printp(
        "You take the right path, hoping it leads to a safer place.",
        3,
    )
    printppp("You see the", helper, "by the pond and they notice you.", 3)
    printpp(
        helper,
        ": Hello, traveler. It's rare to see humans here. What brings you here?",
        3,
    )
    print("1. Tell the", helper, "about your quest, unsure of their intentions.")
    print("2. Keep your mission a secret and ask the", helper, "for guidance.")
    choice = get_choice("Enter 1 or 2 based on your choice: ", ["1", "2"])
    if choice == "1":
        tell()
    elif choice == "2":
        keep()


def tell():
    global score
    score -= 1
    print("score:", score)
    printppp(
        "# You share everything with the",
        helper,
        "and they kindly lead you to a tree with a door carved in its trunk.",
        3,
    )
    printpp(
        helper,
        ": You're propably our savior from the drought curse An evil wizard has cast on us.",
        2,
    )
    printp(
        "The Tree of Whispers. It holds many secrets and to access them, you must answer a riddle.",
        3,
    )
    print("Riddle: I speak without a mouth and hear without ears.")
    printp("I have no body, but I come alive with wind. What am I?", 4)
    print("1. Guess An Echo.")
    print("2. Guess A Whisper.")
    choice = get_choice("Enter 1 or 2 based on your choice: ", ["1", "2"])
    if choice == "1":
        echo()
    elif choice == "2":
        whisper()


def keep():
    global score
    score += 1
    print("score:", score)
    printppp(
        "You decide to keep your mission a secret for now and ask the",
        helper,
        "for guidance.",
        3,
    )
    printppp(
        "The",
        helper,
        "kindly leads you to a tree with a door carved in its trunk.",
        2,
    )
    printpp(
        helper,
        ": The Tree of Whispers. It holds many secrets and to access them, you must answer a riddle",
        2,
    )
    print("Riddle: I speak without a mouth and hear without ears.")
    printp(" I have no body, but I come alive with wind. What am I?", 4)
    print("1. Guess An Echo.")
    print("2. Guess A Whisper.")
    choice = get_choice("Enter 1 or 2 based on your choice: ", ["1", "2"])
    if choice == "1":
        echo()
    elif choice == "2":
        whisper()


def echo():
    global score
    score += 1
    print("score:", score)
    printp("You take a deep breath and confidently say, An Echo.", 4)
    printppp(
        "The", helper, "smiles and the door to the Tree of Whispers creaks open", 2
    )
    printppp(
        "You thank the",
        helper,
        "and take the staircase. You find a dim chamber with money and a shimmering book on a pedestal.",
        3,
    )
    print("1. Take the money and leave")
    print("2. Approach the pedestal and open the shimmering book.")
    choice = get_choice("Enter 1 or 2 based on your choice: ", ["1", "2"])
    if choice == "1":
        money()
    elif choice == "2":
        book()


def whisper():
    global score
    global player_inventory
    score = 0
    print("score:", score)
    printpp(
        "Wrong answer. the door doesn't open and you go back home defeated.",
        3,
    )
    printp("The forest dies from drought", 3)
    print("Your score:", score)
    print("Your inventory:", player_inventory)
    play_again()


def money():
    global score
    global player_inventory
    global cash
    score = 0
    print("score:", score)
    printp(
        "You took the money and escaped leaving the forest die.",
        2,
    )
    print("Coward :)")
    player_inventory.append(cash)
    print("Your score:", score)
    print("Your inventory:", player_inventory)
    play_again()


def book():
    global score
    score += 2
    print("score:", score)
    printp(
        "# You approach the shimmering book, open it, and find pages with shifting illustrations and cryptic text.",
        2,
    )
    printp("Suddenly, the room is filled with a warm, golden light", 2)
    printp("The book presents you two choices", 2)
    print("1. Control fire")
    print("2. Control water")
    choice = get_choice("Enter 1 or 2 based on your choice: ", ["1", "2"])
    if choice == "1":
        fire()
    elif choice == "2":
        water()


def fire():
    global score
    global player_inventory
    player_inventory.append("Fire ability")
    score -= 1
    print("score:", score)
    printp("Despite that you know about the drought spell you chose fire...", 3)
    printppp("The", helper, "comes in looking anxious and gives you a box!", 2)
    printpp(helper, ": Take that, it may help you!", 3)
    printp("Will you take the box?", 2)
    print("1. Yes")
    print("2. No")
    choice = get_choice("Enter 1 or 2 based on your choice: ", ["1", "2"])
    if choice == "1":
        box()
    elif choice == "2":
        nbox()


def water():
    global score
    global player_inventory
    player_inventory.append("Water ability")
    score += 2
    print("score:", score)
    printp("You chose water, good choice!", 2)
    printppp("The", helper, "comes in looking anxious and gives you a box!", 2)
    printpp(helper, ": Take that, it may help you!", 3)
    printp("Will you take the box?", 2)
    print("1. Yes")
    print("2. No")
    choice = get_choice("Enter 1 or 2 based on your choice: ", ["1", "2"])
    if choice == "1":
        box()
    elif choice == "2":
        nbox()


# function for choosing not to take the box
def nbox():
    global score
    score -= 1
    print("score:", score)
    printppp(
        "You didn't take the box and the",
        helper,
        "looks more anxious more than before...",
        2,
    )
    printpp(
        helper,
        ": The evil wizard is casting spells and the creatures of the forest are in danger! We should hurry to save them!",
        3,
    )
    print("1. Follow the", helper, "to confront the sorcerer directly.")
    print("2. Seek allies in the forest to help you combat the sorcerer.")
    choice = get_choice("Enter 1 or 2 based on your choice: ", ["1", "2"])
    if choice == "1":
        confront()
    elif choice == "2":
        seeka()


def box():
    global score
    score += 1
    print("score:", score)
    global player_inventory
    player_inventory.append(weapon)
    printp("The box has...", 3)
    printpp(weapon, "!!", 2)
    printppp("The", helper, "looks less anxious", 1)
    printpp(
        helper,
        ": The evil wizard is casting spells and the creatures of the forest are in danger! We should hurry to save them!",
        3,
    )
    print("1. Follow the", helper, "to confront the sorcerer directly.")
    print("2. Seek allies in the forest to help you combat the sorcerer.")
    choice = get_choice("Enter 1 or 2 based on your choice: ", ["1", "2"])
    if choice == "1":
        confront()
    elif choice == "2":
        seeka()


def confront():
    global score
    global player_inventory
    global food
    global cash
    global jewel
    if "Fire ability" in player_inventory:
        # checks if you got any weapons since fire abilities wont help much becuase of the drought
        # but if you got items you can beat the wizard but not save the forest from the drought
        for item in player_inventory:
            if item in magical_weapon:
                score = +1
                print("score:", score)
                printppp(
                    "you used the",
                    item,
                    "to confront the evil wizard and won but the forest withered from the drought",
                    3,
                )
                print("at least you have tried and the forest gave you some jewels")
                player_inventory.append(jewel)
                print("Your score:", score)
                print("Your inventory:", player_inventory)
                play_again()
            elif item not in magical_weapon:
                printp(
                    "you confronted the wizard without seeking allies or at least taking the box... The wizard beat you",
                    3,
                )
                printp("You've died :()")
                print("Your inventory: None... you're dead.")
                print("Your score:", score)
                play_again()

    elif "Water ability" in player_inventory:
        score = +2
        # checks if you got weapons in ur inventory,
        # but you dont need a weapon to win
        for item in player_inventory:
            if item in magical_weapon:
                score = +1
                print("score:", score)
                print(
                    "you used the",
                    item,
                    "to confront the evil wizard and won against him! YAY :D",
                )
                printp("The forest is saved and you are hailed as a hero!", 3)
                printp("Gifts: cash, food, jewels", 2)
                player_inventory.append(cash)
                player_inventory.append(food)
                player_inventory.append(jewel)
                print("Your score:", score)
                print("Your inventory:", player_inventory)
                play_again()
            elif item not in magical_weapon:
                score = -1
                print("score:", score)
                printp(
                    "You tried to defeat the wizard with your abilities, but without a weapon or allies!",
                    3,
                )
                printppp(
                    "The", helper, "tries to help you retreat before you die...", 3
                )
                printppp(
                    "# Will you continue fighting or seek allies with the",
                    helper,
                    "?",
                    3,
                )
                print("1.Seek allies")
                print("2.Continue fighting.")
                choice = get_choice("Enter 1 or 2 based on your choice: ", ["1", "2"])
                if choice == "1":
                    seeka()
                elif choice == "2":
                    printp("# You fought on, but eventually grew tired and died.", 3)
                    print("Your inventory: None... you're dead.")
                    print("Your score:", score)
                    play_again()


# function for seeking allies decisions
def seeka():
    global score
    global player_inventory
    global food
    global cash
    global jewel
    score += 1
    print("score:", score)
    printp("You seek allies in the forest to help fight the sorcerer.", 3)
    printp(
        "You gather brave creatures and head to the sorcerer's lair together.",
        3,
    )
    printp(
        "A fierce battle ensues. With your skills and allies, you defeat the sorcerer and lift the drought.",
        3,
    )
    printp("The forest is saved and you are hailed as a hero!", 3)
    player_inventory.append(cash)
    player_inventory.append(food)
    player_inventory.append(jewel)
    printp("Gifts: cash, food, jewels", 2)
    print("Your score:", score)
    print("Your inventory:", player_inventory)
    play_again()


start_game()
