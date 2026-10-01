import random


class GameManager:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def display_board(self):
        print()
        print(self.board[0], "|", self.board[1], "|", self.board[2])
        print("--+---+--")
        print(self.board[3], "|", self.board[4], "|", self.board[5])
        print("--+---+--")
        print(self.board[6], "|", self.board[7], "|", self.board[8])
        print()

    def get_available_moves(self):
        return [i for i in range(9) if self.board[i] == " "]

    def make_move(self, position, player):
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def check_winner(self):
        winning_patterns = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in winning_patterns:
            if self.board[a] != " ":
                if self.board[a] == self.board[b] == self.board[c]:
                    return self.board[a]

        if " " not in self.board:
            return "Draw"

        return None


class GameAgent:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def choose_move(self, game):
        available_moves = game.get_available_moves()

        if available_moves:
            return random.choice(available_moves)

        return None


def play_game():
    game = GameManager()

    agent_x = GameAgent("Agent X", "X")
    agent_o = GameAgent("Agent O", "O")

    agents = {
        "X": agent_x,
        "O": agent_o
    }

    while True:
        game.display_board()

        current_agent = agents[game.current_player]

        print(current_agent.name, "is playing...")

        move = current_agent.choose_move(game)

        if move is None:
            break

        game.make_move(move, current_agent.symbol)

        result = game.check_winner()

        if result:
            game.display_board()
            print("Game Result:", result)
            break

        if game.current_player == "X":
            game.current_player = "O"
        else:
            game.current_player = "X"


if __name__ == "__main__":
    play_game()