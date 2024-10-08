from constants import *
from graph import *

import math


class TicTacToe:
    def __init__(self, size) -> None:
        self.size = size
        self.graph = Graph(size)

    def clone(self) -> 'TicTacToe':
        clone = TicTacToe(self.size)
        clone.graph = self.graph.clone()

        return clone

    def reset(self, new_size=None) -> None:
        self.size = self.size if new_size is None else new_size
        self.graph = Graph(self.size)

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

    def result(self, action) -> 'TicTacToe':
        """
        Returns the board that results from making move (row, col) on the board.
        """

        if action not in self.actions():
            return

        row, col = action
        new_state = self.clone()

        new_state.graph.grid[row][col] = self.player()

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

    def utility(self):
        """
        Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
        """

        result = self.winner()

        if result == X:
            return 1
        elif result == O:
            return -1
        else:
            return 0

    def minimize(self):
        v = math.inf
        if self.terminal():
            return self.utility(), None

        for action in self.actions():
            new_val, _ = self.result(action).maximize()
            if new_val < v:
                v = new_val
                picked = action

                if v == -1:
                    return v, picked

        return v, picked

    def maximize(self):
        v = -math.inf
        if self.terminal():
            return self.utility(), None

        for action in self.actions():
            new_val, _ = self.result(action).minimize()
            if new_val > v:
                v = new_val
                picked = action

                if v == 1:
                    return v, picked

        return v, picked

    def minimax(self):
        """
        Returns the optimal action for the current player on the board.
        """
        if self.player() == X:
            _, picked = self.maximize()
        else:
            _, picked = self.minimize()

        return picked
