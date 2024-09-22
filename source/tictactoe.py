from constants import *
from graph import *


class TicTacToe:
    def __init__(self, size) -> None:
        self.size = size
        self.graph = Graph(size)

    # def reset(self, new_size=None) -> None:
    #     self.size = self.size if new_size is None else new_size
    #     self.graph = Graph(self.size)

    def player(self) -> str:
        """
        Returns the player who has the next move.
        """

        o_count = sum([row.count(O) for row in self.graph.grid])
        x_count = sum([row.count(X) for row in self.graph.grid])

        return X if o_count >= x_count else O

    def actions(self) -> set[tuple[int, int]]:
        """
        Returns set of all possible actions (row, col) available on the board.
        """

        possible = set()
        for row in range(self.size):
            for col in range(self.size):
                if self.graph.is_empty(row, col):
                    possible.add((row, col))

        return possible

    def result(self, action) -> Graph:
        """
        Returns the board that results from making move (row, col) on the board.
        """

        if action not in self.actions():
            return

        row, col = action
        new_state = self.graph.clone()
        new_state[row][col] = self.player()

        return new_state

    def winner(self):
        """
        Returns the winner of the game, if there is one.
        """

        def check(option, player):
            for cell in option:
                if cell != player:
                    return False

            return True

        possible = [row for row in self.graph.grid] + \
            [list(col) for col in zip(*self.graph.grid)]
        possible += [[self.graph.grid[i][i]
                      for i in range(self.size)]] + [[self.graph.grid[i][self.size-1-i] for i in range(self.size)]]

        for player in (X, O):
            for option in possible:
                if check(option, player):
                    return player

        return None

    def terminal(self):
        """
        Returns True if game is over, False otherwise.
        """

        if not self.graph.is_full():
            return self.winner() is not None

        return True
