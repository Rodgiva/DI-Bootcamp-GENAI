def display_grid(grid_state:list = []):
    line = "*****************"
    line_ = "*  ---|---|---  *"
    line1 = "*     |   |     *"
    line2 = "*     |   |     *"
    line3 = "*     |   |     *"
    for state_line in grid_state:
        if state_line[0] == 1:
            index = (state_line[1]*4)
            line1 = line1[:index] + state_line[2] + line1[index + 1:]
        elif state_line[0] == 2:
            index = (state_line[1]*4)
            line2 = line2[:index] + state_line[2] + line2[index + 1:]
        elif state_line[0] == 3:
            index = (state_line[1]*4)
            line3 = line3[:index] + state_line[2] + line3[index + 1:]
    print("\nTIC TAC TOE")
    print(f"{line}\n{line1}\n{line_}\n{line2}\n{line_}\n{line3}\n{line}\n")

def check_win(state_game:list)->bool:
    for i in range(0,2):
        for j in range(1,4):
            for player in ["X", "O"]:
                if len([move for move in state_game
                        if move[i] == j and move[2] == player]) == 3:
                    return False
    for player in ["X", "O"]:
        if len([move for move in state_game
                if ((move[0] == 1 and move[1] == 1)
                    or (move[0] == 2 and move[1] == 2)
                    or (move[0] == 3 and move[1] == 3))
                    and move[2] == player]) == 3:
            return False
    for player in ["X", "O"]:
        if len([move for move in state_game
                if ((move[0] == 1 and move[1] == 3)
                    or (move[0] == 2 and move[1] == 2)
                    or (move[0] == 3 and move[1] == 1))
                    and move[2] == player]) == 3:
            return False
    return True

def check_duplicate(state_game: list, coordonate: list) -> bool:
    return coordonate in [state[:-1] for state in state_game]

def get_valid_input(inp):
    while True:
        res = input(inp)
        try:
            return int(res)
        except ValueError:
            print("Please enter a valid coordonate.")

def game_loop():
    state_game = []
    print("\nWelcome to TIC TAC TOE!")
    display_grid()
    turn = 0
    player = ""
    while check_win(state_game):
        if turn == 9:
            print("This is a tie.")
            return
        turn += 1
        if turn % 2 == 0:
            player = "O"
        else:
            player = "X"
        print(f"Player {player}'s turn...")
        row = get_valid_input("Enter row: ")
        column = get_valid_input("Enter column: ")
        if check_duplicate(state_game, [row, column]):
            print("\n!!! This cell is already taken. !!!\n")
            turn -= 1
            continue
        state_game.append([row, column, player])
        display_grid(state_game)
    print(f"The player {player} won!")
game_loop()