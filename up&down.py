import random

def get_initial_points():
    while True:
        try:
            points = float(input("Enter the points you want to use to play (minimum 10 points): "))
            if points < 10:
                print("Points are not up to ten. Please enter a number higher than 10.")
            else:
                return points
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def play_game():
    user_options = ["up", "down"]
    computer_options = ["up", "down", "center"]
    
    points = get_initial_points()
    print("Welcome to my up and down game!")

    while points >= 10:
        user_choice = input("Choose 'up' or 'down': ").lower()
        if user_choice not in user_options:
            print("Invalid choice. Please choose 'up' or 'down'.")
            continue
        
        computer_choice = random.choice(computer_options)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            points *= 2
            print(f"Congratulations! Your points have doubled. You now have {points} points.")
        else:
            points -= 10
            print(f"Sorry, you lost 10 points. You now have {points} points.")
        
        if points < 10:
            print("You don't have enough points to play.")
            break
        
        continue_game = input("Do you want to continue? (yes/no): ").lower()
        if continue_game != "yes":
            break

    print(f"Game over! You ended with {points} points.")

play_game()
