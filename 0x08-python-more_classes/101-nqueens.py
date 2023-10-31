#!/usr/bin/python3
import sys

"""Define a class for a chessboard board to solve the 8 gueens puzzle"""


class Board:
    """Represents a chessboard"""

    def __init__(self, n):
        """Initializes the board with the given size"""
        if n < 4:
            raise ValueError("N must be at least 4")
        self.n = n
        self.cells = [[0 for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def is_valid(self, row, col):
        """Check if a queen can be placed in the given row, column, and diagonals"""
        for i in range(self.n):
            if self.cells[i][col] == 1:
                return False

        for j in range(self.n):
            if self.cells[row][j] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.cells[i][j] == 1:
                return False

        for i, j in zip(range(row, self.n), range(col, self.n)):
            if self.cells[i][j] == 1:
                return False

        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.cells[i][j] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.cells[i][j] == 1:
                return False

        return True

    def solve_n_queens_helper(self, row):
        """Recursively solves the n-queens problem"""
        if row == self.n:
            self.solutions.append([row[:] for row in self.cells])
            return

        for col in range(self.n):
            if self.is_valid(row, col):
                self.cells[row][col] = 1
                self.solve_n_queens_helper(row + 1)
                self.cells[row][col] = 0

    def solve_n_queens(self):
        """Solves the n-queens problem and returns a list of solutions"""
        self.solutions = []
        self.solve_n_queens_helper(0)
        return self.solutions

    def get_position_of_queens(self):
        """Returns a list of lists of tuples representing the positions of the queens"""
        result: list[list[tuple[int, int]]] = []
        for i in range(len(self.solutions)):
            result.append([])
            for row in range(self.n):
                for col in range(self.n):
                    if self.solutions[i][row][col] == 1:
                        result[i].append([row, col])

        return result


def main(n):
    """Prints all solutions to the n-queens problem"""
    board = Board(n)
    board.solve_n_queens()
    for solution in board.get_position_of_queens():
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    else:
        try:
            n = int(sys.argv[1])
            if n < 4:
                print("N must be at least 4")
                exit(1)
            else:
                main(n)
        except ValueError:
            print("N must be a number")
            exit(1)
