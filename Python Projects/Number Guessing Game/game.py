import random
random.seed()

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("In this game, the AI will choose a random number between 1 and 100. Your objective is to guess that number!")
    print("Begin by choosing a difficulty to determine how many changes you get!")
    print("Try to guess the number in as few tries as possible.")

def choose_difficulty():
    print("Please select the difficulty level")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print()
    user_choice_str = input("Enter your choice: ")
    user_choice = int(user_choice_str) #We need to ensure that a number is entered not a random word
    return user_choice

def set_chances(user_choice):
    if user_choice == 1:
        chance_amount = 10
    elif user_choice == 2:
        chance_amount = 5
    elif user_choice == 3:
        chance_amount = 3
    return chance_amount

def randomise_number():
    return random.randrange(1, 101)

def victory_message():
    print("You win!")

def loss_message(answer):
    print("You lose. The answer was " + str(answer))

print(randomise_number())

def main():
    user_guess = 0
    chance_amount = 0
    random_number = randomise_number()
    welcome_message()
    user_choice = choose_difficulty()
    while user_choice <= 0 or user_choice > 3:
        print("Invalid input. Please try again.")
        user_choice = int(input("Enter your choice: "))
    
    chance_amount = set_chances(user_choice)
    random_number = randomise_number()
    while chance_amount > 0:
        user_guess = int(input("Enter your guess: "))
        if user_guess == random_number:
            victory_message()
            break
        else:
            chance_amount -= 1
            print("Incorrect guess.")
            if chance_amount > 0:
                print(f"You have {chance_amount} chances left.")
                if user_guess > random_number:
                    print("The secret number is smaller than your guess")
                else:
                    print("The secret number is larger than your guess")
            else:
                loss_message(random_number)

main()