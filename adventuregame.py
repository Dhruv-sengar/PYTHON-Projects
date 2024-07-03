import shutil
def get_terminal_width():
    """Get the width of the terminal window"""
    return shutil.get_terminal_size().columns

def center_text(text):
    """Center text in the terminal"""
    width = get_terminal_width()
    padding = (width - len(text)) // 2
    return ' ' * padding + text

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print(colors.BOLD + colors.BLUE + center_text("WELCOME TO THE WORLD OF ADVENTURE!!!!!!!!!!!") + colors.END)
print(" ")

import time

def print_with_delay(text, delay=1):
    print(text)
    time.sleep(delay)

def intro():
    print_with_delay("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_with_delay("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")
    print_with_delay("In front of you is a house.")
    print_with_delay("To your right is a dark cave.")
    print_with_delay("In your hand you hold your trusty (but not very effective) dagger.\n")

def house():
    print_with_delay("You approach the door of the house.")
    print_with_delay("You are about to knock when the door opens and out steps a fairie.")
    print_with_delay("Eep! This is the fairie's house!")
    print_with_delay("The fairie attacks you!\n")
    if "sword" in inventory:
        fight("fairie")
    else:
        print_with_delay("You feel a bit under-prepared for this, what with only having a tiny dagger.\n")
        choice = input("Would you like to (1) fight or (2) run away? ")
        if choice == "1":
            fight("fairie")
        elif choice == "2":
            field()
        else:
            print_with_delay("Invalid choice. The fairie attacks you and you lose the fight.")
            game_over()

def cave():
    print_with_delay("You peer cautiously into the cave.")
    print_with_delay("It turns out to be only a very small cave.")
    print_with_delay("Your eye catches a glint of metal behind a rock.")
    print_with_delay("You have found the magical Sword of Ogoroth!\n")
    inventory.append("sword")
    print_with_delay("You discard your silly old dagger and take the sword with you.")
    print_with_delay("You walk back out to the field.\n")
    field()

def fight(enemy):
    if "sword" in inventory:
        print_with_delay(f"As the {enemy} moves to attack, you unsheath your new sword.")
        print_with_delay(f"The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
        print_with_delay(f"But the {enemy} takes one look at your shiny new toy and runs away!")
        print_with_delay(f"You have rid the town of the {enemy}. You are victorious!")
        play_again()
    else:
        print_with_delay(f"You do your best... but your dagger is no match for the {enemy}.")
        print_with_delay("You have been defeated!")
        game_over()

def field():
    print_with_delay("Enter 1 to knock on the door of the house.")
    print_with_delay("Enter 2 to peer into the cave.")
    print_with_delay("What would you like to do?")
    choice = input("(Please enter 1 or 2.) ")
    if choice == "1":
        house()
    elif choice == "2":
        cave()
    else:
        print_with_delay("Invalid choice.")
        field()

def play_again():
    choice = input("Would you like to play again? (yes/no) ").lower()
    if choice == "yes":
        start_game()
    elif choice == "no":
        print_with_delay("Thanks for playing! Goodbye.")
    else:
        print_with_delay("Invalid choice.")
        play_again()

def game_over():
    print_with_delay("Game Over.")
    play_again()

def start_game():
    global inventory
    inventory = []
    intro()
    field()

start_game()
