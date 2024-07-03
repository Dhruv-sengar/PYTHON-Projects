import random
print("WELCOME TO NUMBER GUESSING GAME!!!")

playing = input("DO YOU WANT TO PLAY THE GAME :- ")
if playing.lower() == "yes":
    print("THE GAME BEGINS!!!!!!!!")
    print("Let's start the game!")
    random_number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10 :- "))
    while guess != random_number:
        if guess < random_number:
            print("Your guess is too low")
        elif guess > random_number:
            print("Your guess is too high")
        guess = int(input("Guess a number between 1 and 10 :- "))
    print("Congratulations! You guessed the correct number")
else:
    print("NO WORRIES!!!")
    print("Have a good day!!")