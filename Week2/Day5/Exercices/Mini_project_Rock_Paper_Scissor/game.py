import random as r

class Game():
    _rock_paper_scissors_list = ["rock", "paper", "scissors"]
    _win_rules = {
        "win": [
            (1, 0),
            (2, 1),
            (0, 2),
        ],
        "draw": [
            (1, 1),
            (2, 2),
            (0, 0),
        ],
        "loss": [
            (0, 1),
            (1, 2),
            (2, 0),
        ],
    }

    def __init__(self):
        self.win:int = 0
        self.draw:int = 0
        self.loss:int = 0

    @staticmethod
    def get_user_item()->str:
        choice = int(input(f"What is your move?\n1. Rock\n2. Paper\n3. Scissors\n"))
        return Game._rock_paper_scissors_list[choice-1]

    @staticmethod
    def get_computer_item()->str:
        return r.choice(Game._rock_paper_scissors_list)

    def get_game_result(self, user_item:str, computer_item:str):
        key_item_user = Game._rock_paper_scissors_list.index(user_item)
        key_item_computer = Game._rock_paper_scissors_list.index(computer_item)
        if (key_item_user, key_item_computer) in Game._win_rules["win"]:
            self.win += 1
            return "win"
        elif (key_item_user, key_item_computer) in Game._win_rules["loss"]:
            self.loss += 1
            return "loss"
        else:
            self.draw += 1
            return "draw"

    def play(self):
        user_item = Game.get_user_item()
        computer_item = Game.get_computer_item()

        print(f"{user_item}(you) - {computer_item}(computer)")
        print(self.get_game_result(user_item, computer_item))