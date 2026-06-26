from random import choice

game_board = ['', '', '', '', '', '', '', '', '']
available_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def show_board():
    print(f" {game_board[0]} | {game_board[1]} | {game_board[2]}")
    print("---------------------")
    print(f" {game_board[3]} | {game_board[4]} | {game_board[5]}")
    print("---------------------")
    print(f" {game_board[6]} | {game_board[7]} | {game_board[8]}")

# User picks X or O
while True:
    user_char = input("Pick X or O: ").upper()

    # Input Validation
    if user_char not in ["X", "O"]:
        print("Please enter either X or O")
        continue

    # Assigns opposite char to aI
    else:
        if user_char == "X":
            ai_char = "O"
        elif user_char == "O":
            ai_char = "X"
        break

# Game loop
rounds_played = 0
game = True
while game:

    # User move and validation
    try:
        user_move = int(input(f"Enter a move from 1 to 9: "))
    except ValueError:
        continue
    except IndexError:
        continue

    if user_move not in range(1, 10):
        print(f"Please enter a move from 1 to 9")
        continue

    # Checks if the user move is available
    if (user_move - 1) not in available_indexes:
       print("This move is not available")
       continue

    # Writes uses move on the board
    else:
        game_board[user_move - 1] = user_char
        available_indexes.remove(user_move - 1)
        rounds_played += 1

        # AI plays
        ai_move = choice(available_indexes)
        game_board[ai_move] = ai_char
        available_indexes.remove(ai_move)


    # Winning conditions
    if rounds_played >= 3:
        print(rounds_played)
        row1 =  [game_board[0], game_board[1], game_board[2]]
        row2 = [game_board[3], game_board[4], game_board[5]]
        row3 = [game_board[6], game_board[7], game_board[8]]
        col1 = [game_board[0], game_board[3], game_board[6]]
        col2 = [game_board[1], game_board[4], game_board[7]]
        col3 = [game_board[2], game_board[5], game_board[8]]
        diagonal1 = [game_board[0], game_board[4], game_board[8]]
        diagonal2 = [game_board[2], game_board[4], game_board[6]]

        lines = [row1, row2, row3, col1, col2, col3, diagonal1, diagonal2]
        for line in lines:
            is_uniform = all(element == line[0] for element in line)
            if is_uniform and line[0] == user_char:
                print("Player wins!")
                game = False
            if is_uniform and line[0] == ai_char:
                print("AI wins!")
                game = False
            if not is_uniform and len(available_indexes) == 0:
                print("Draw!")
            break


    show_board()

