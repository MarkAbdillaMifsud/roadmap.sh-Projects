import random
import csv
random.seed()

def welcome_message():
    """Prints out welcome message when application launches"""
    print("Welcome to the Number Guessing Game!")
    print("In this game, the AI will choose a random number between 1 and 100. Your objective is to guess that number!")
    print("Begin by choosing a difficulty to determine how many changes you get!")
    print("Try to guess the number in as few tries as possible.")

def choose_difficulty():
    """Processes user's difficulty choice"""
    print("Please select the difficulty level")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print()
    user_choice_str = input("Enter your choice: ")
    user_choice = int(user_choice_str) #We need to ensure that a number is entered not a random word
    return user_choice

def set_chances(user_choice):
    """Sets guess amount based on difficulty choice"""
    if user_choice == 1:
        chance_amount = 10
    elif user_choice == 2:
        chance_amount = 5
    elif user_choice == 3:
        chance_amount = 3
    return chance_amount

def randomise_number():
    """Generate a random number"""
    return random.randrange(1, 101)

def score_penalty(user_choice):
    """Establishes penalty depending on difficulty choice"""
    if user_choice == 1:
        score_penalty = 50
    elif user_choice == 2:
        score_penalty = 25
    elif user_choice == 3:
        score_penalty = 10
    return score_penalty

def process_guess(chance_amount, random_number, user_choice):
    """Main guessing functionality"""
    final_score = 600
    while chance_amount > 0:
        user_guess = int(input("Enter your guess: "))
        if user_guess == random_number:
            victory_message(final_score)
            break
        else:
            chance_amount -= 1
            final_score -= score_penalty(user_choice)
            print("Incorrect guess.")
            if chance_amount > 0:
                print(f"You have {chance_amount} chances left.")
                if user_guess > random_number:
                    print("The secret number is smaller than your guess")
                else:
                    print("The secret number is larger than your guess")
            else:
                loss_message(random_number)

def victory_message(final_score):
    """Prints win message and gets username of player"""
    print("You win!")
    username = input("Enter your username to record your score: ")
    update_scores(username, final_score)

def loss_message(answer):
    """Prints loss message"""
    print("You lose. The answer was " + str(answer))

def get_scores(filename="scores.csv"):
    """Loads scores from a CSV file and returns them as a list of tuples"""
    scores =[]
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    scores.append((row[0], int(row[1])))
    except FileNotFoundError:
        print("No scores file found. Starting fresh.")
    except Exception as e:
        print("Error loading scores:", e)
    return scores

def update_scores(username, score, filename="scores.csv"):
    """Update the CSV file by adding the new score to the user's previous score. If the user doesn't exist, create a new entry"""
    scores={}
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    scores[row[0]] = int(row[1])
    except FileNotFoundError:
        scores = {}
    
    if username in scores:
        scores[username] += score
    else:
        scores[username] = score
    
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user, total in scores.items():
                writer.writerow([user, total])
    except Exception as e:
        print("Error saving score:", e)

def is_continue(user_progression_choice):
    """Processes whether user wants to try again"""
    while user_progression_choice.upper() != "Y" and user_progression_choice.upper() != "N":
        if user_progression_choice.upper() == "Y":
            return True
        elif user_progression_choice.upper() == "N":
            return False
        else:
            user_progression_choice = input("Invalid choice. Please try again: ")

def main():
    playing = True
    user_guess = 0
    chance_amount = 0
    welcome_message()
    scores = get_scores()
    if scores:
        print("\nCurrent High Scores:")
        for username, score in scores:
            print(f"{username}: {score}")
    else:
        print("\nNo high scores yet. Be the first to set one!")
    while playing:
        random_number = randomise_number()
        user_choice = choose_difficulty()
        while user_choice <= 0 or user_choice > 3:
            print("Invalid input. Please try again.")
            user_choice = int(input("Enter your choice: "))
        chance_amount = set_chances(user_choice)
        random_number = randomise_number()
        process_guess(chance_amount, random_number, user_choice)
        user_progression_choice = input("Would you like to play another round? (Y/N)")
        playing = is_continue(user_progression_choice)
        if not playing:
            exit()

main()