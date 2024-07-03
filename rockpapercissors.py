import shutil
import random

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

# Example usage
text = "WELCOME TO THE STONE, PAPER AND SCISSORS GAME!!"
print(center_text(colors.BOLD + colors.CYAN + text + colors.END))

playing = input("DO YOU WANT TO PLAY THE GAME:- ")
if playing.lower() == "yes":
    print(center_text(colors.MAGENTA + "THE GAME BEGINS!!!!!!!!" + colors.END))
    print(center_text(colors.UNDERLINE + colors.YELLOW + "Let's start the game!" + colors.END))
    p1_score = 0
    p2_score = 0

    player1 = input("ENTER YOUR NAME:- ")
    
    while p1_score < 3 and p2_score < 3:
        print(f"\n{center_text(colors.BOLD + colors.GREEN + f'{player1}\'s Turn!!' + colors.END)}")
        p1_choice = input("Enter your choice (stone/paper/scissors):- ").lower()
        
        if p1_choice in ["stone", "paper", "scissors"]:
            print(center_text(colors.BOLD + colors.GREEN + f"{player1} chose {p1_choice}" + colors.END))
            p2_choice = random.choice(["stone", "paper", "scissors"])
            print(center_text(colors.BOLD + colors.RED + f"BOT chose {p2_choice}" + colors.END))
            
            if p1_choice == p2_choice:
                print(center_text(colors.BOLD + colors.YELLOW + "IT'S A TIE" + colors.END))
            elif (p1_choice == "stone" and p2_choice == "scissors") or \
                 (p1_choice == "paper" and p2_choice == "stone") or \
                 (p1_choice == "scissors" and p2_choice == "paper"):
                print(center_text(colors.BOLD + colors.YELLOW + f"{player1} WINS!!" + colors.END))
                p1_score += 1
            else:
                print(center_text(colors.BOLD + colors.YELLOW + "BOT WINS!" + colors.END))
                p2_score += 1

            print(center_text(colors.BOLD + colors.YELLOW + f"{player1}'s score: {p1_score}, BOT's score: {p2_score}" + colors.END))
        else:
            print(center_text(colors.BOLD + colors.RED + "Invalid choice! Please choose stone, paper, or scissors." + colors.END))
    
    if p1_score == 3:
        print(center_text(colors.BOLD + colors.GREEN + f"{player1} WINS THE GAME!" + colors.END))
    else:
        print(center_text(colors.BOLD + colors.RED + "BOT WINS THE GAME!" + colors.END))
else:
    print(center_text(colors.BOLD + colors.RED + "NO WORRIES!!" + colors.END))
    print(center_text(colors.BOLD + colors.GREEN + "HAVE A GOOD DAY!!!!!!!!" + colors.END))
