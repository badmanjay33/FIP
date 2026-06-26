from random import choice
"""
CONSTANTS & Variables
options: list[str] - a list of the options the cpu could choose.
cpu_choice: str - a random selection from the options list.
cpu_: str - the first letter of the choice used for checking conditions
user_choice: str - a move picked by user ("P", "R", "S) for moves and "Q" for quit.
"""

# CPU Options
OPTIONS = ["Rock", "Paper", "Scissors"]

while True:
    # CPU Choice
    cpu_choice = choice(OPTIONS)
    cpu_ = cpu_choice[0]

    # User input
    user_choice = input("Pick a move! [R]ock [P]aper [S]cissor [Q]uit: ").upper()

    # Exit condition
    if user_choice == "Q":
        print("Goodbye!")
        break # Exit the loop

    # User input validation
    if user_choice not in ["R", "P", "S",]:
        print("Please enter either 'R', 'P', 'S' \n")
        continue

    # Game outcomes
    # Draw condition: Checks only the first letters incase the user chooses to enter only the first key.
    if user_choice[0] == cpu_:
        print(f"CPU also picked {cpu_choice}.\n Draw! \n")

    # Conditions for user to win
    elif ((user_choice == "R" and cpu_ == "S") or
          (user_choice == "S" and cpu_ == "P") or
          (user_choice == "P" and cpu_ == "R")):
        print(f"CPU picks {cpu_choice} You win! \n")

    # CPU wins
    else:
        print(f"CPU picks {cpu_choice} CPU wins \n")