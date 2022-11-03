import os
# Variables
field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
valid_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player_symbols = ["X", "O"]
turn = 1
game_going = False
player = player_symbols[0]
# Functions


def clear():
    os.system("clear")


def print_playfield():
    print(f" {field[0]} | {field[1]} | {field[2]}\n "
          "---------\n"
          f" {field[3]} | {field[4]} | {field[5]}\n "
          "---------\n"
          f" {field[6]} | {field[7]} | {field[8]} ")


def place_player_symbol(position, player):
    global turn

    position_int = int(position) - 1
    field[position_int] = player

    turn += 1

    print_playfield()


0


def check_winner(player):
    global game_going

    if field[0] == player and field[1] == player and field[2] == player:
        game_going = False
        clear()
        print(f"{player} won the game.")
        reset_game()

    elif field[3] == player and field[4] == player and field[5] == player:
        game_going = False
        clear()
        print(f"{player} won the game.")
        reset_game()

    elif field[6] == player and field[7] == player and field[8] == player:
        game_going = False
        clear()
        print(f"{player} won the game.")
        reset_game()

    elif field[0] == player and field[3] == player and field[6] == player:
        game_going = False
        clear()
        print(f"{player} won the game.")
        reset_game()

    elif field[1] == player and field[4] == player and field[7] == player:
        game_going = False
        clear()
        print(f"{player} won the game.")
        reset_game()

    elif field[2] == player and field[5] == player and field[8] == player:
        game_going = False
        clear()
        print(f"{player} won the game.")
        reset_game()


def reset_game():
    global turn, field, player
    turn = 0
    field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = player_symbols[0]


# Game Loop
print("Welcome to my Tic-Tac-Toe game! Are you ready?")
start_game = input("Do you want to start the game? 'Y' or 'N'. ").lower()

if start_game == "y":
    game_going = True

    print("Lets  get started! Here is the playfield!")

    print_playfield()

else:
    game_going = False


while game_going:

    if turn == 10:
        game_going = False
        clear()
        print("No one wins! Game Over!")

    else:

        print(f"Current player: {player} | Current Turn: {turn}")

        question_position = input(
            "Where do you want to put your symbol? (Position 1 - 9)\n")

        clear()

        if question_position not in valid_positions:
            print("Not a position!")
            print_playfield()

        elif int(question_position) > 9 or int(question_position) < 0:
            print("Position does not exist! Please try again!")
            print_playfield()

        elif field[int(question_position) - 1] != " ":
            print("Position already occupied! Please try again!")
            print_playfield()

        else:

            if turn % 2 == 1:
                player = "X"
                place_player_symbol(position=question_position, player=player)
                check_winner(player)
                player = "O"

            elif turn % 2 == 0:
                player = "O"
                place_player_symbol(position=question_position, player=player)
                check_winner(player)
                player = "X"
