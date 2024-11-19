import random

while True:
    # Input validation loop
    while True:
        try:
            choice = int(input('''Select your choice (1, 2, or 3):
               1. Scissors
               2. Paper
               3. Rock
            '''))

            if choice in [1, 2, 3]:
                break  # Exit the validation loop if valid input is provided
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
    
    # Mapping choices
    choices = ('scissors', 'rock', 'paper')
    user_choice = choices[choice - 1]
    comp_choice = random.choice(choices)

    print(f'Your choice is {user_choice} and computer choice is {comp_choice}')

    # Prompt to play again
    want_more = input('Want to play again? Type "y" for Yes: ').strip().lower()
    if want_more != 'y':
        break
