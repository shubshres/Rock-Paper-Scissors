import random

# ascii art for rock
rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# ascii art for paper
paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# ascii art for scissors
scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# rock = 1, paper = 2, scissors = 3
gameImages = [rock, paper, scissors]

# setting boolean to false so we are in an infinite loop until the user wants to quit
quit = bool(False); 

while(quit != True):
    # asking the user what they want to choose
    user_choice = input("\n\nRock, Paper, or Scissors?: ")

    # randomly generating computer's choice
    computer_choice = random.randint(0,2)

    # print what the computer chose
    print("\nThe computer chose: ")
    print(gameImages[computer_choice])

    # comparing the user choice to our three options and assigning an integer to it
    if(user_choice.lower() == "rock"):
        user_choice_int = 0
    elif(user_choice.lower() == "paper"):
        user_choice_int = 1
    elif(user_choice.lower() == "scissors"):
        user_choice_int = 2

    # if that compares the user's answer to the computers
    if(user_choice_int != 0 | user_choice_int != 1 | user_choice_int != 2):
        print("\nInvalid option...\n")
    elif user_choice_int == 0 and computer_choice == 2:
        print("\nYou win!\n")
    elif computer_choice == 0 and user_choice_int == 2:
        print("\nYou lose\n")
    elif computer_choice > user_choice_int:
        print("\nYou lose\n")
    elif user_choice_int > computer_choice:
        print("\nYou win!\n")
    elif computer_choice == user_choice_int:
        print("\nIt's a draw\n")

    # asking the user if they want to continue the game
    continue_game = input("\nDo you want to continue? \n(Enter 'Y' to continue or 'N' to quit): ")

    if(continue_game.lower() == "y"):
        quit = False
    elif(continue_game.lower() == "n"):
        quit = True
