#!/usr/bin/env python3

from numpy import matrix as mt
import cv2

# top = tk.Tk()
# top.mainloop()

# Example sudoku
puzzle = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
          [0, 0, 0, 0, 7, 3, 0, 0, 9],
          [3, 0, 9, 0, 0, 0, 0, 4, 5],
          [4, 9, 0, 0, 0, 0, 0, 0, 0],
          [8, 0, 3, 0, 5, 0, 9, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 3, 6],
          [9, 6, 0, 0, 0, 0, 3, 0, 8],
          [7, 0, 0, 6, 8, 0, 0, 0, 0],
          [0, 2, 8, 0, 0, 0, 0, 0, 0]]

# TODO: Set up image input method, gocr? what is the best ocr?

# TODO: Set up sdk input method


# TODO: Turn input data into a matrix

# TODO: Solve the input puzzle, decide how to deal with multiple solutions.
def possible(board, y, x, n):
    for i in range(9):
        if board[y][i] == n:
            return False
    for i in range(9):
        if board[i][x] == n:
            return False
    xBoxStart = (x // 3) * 3
    yBoxStart = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[yBoxStart + i][xBoxStart + j] == n:
                return False
    return True


def solve(board):
    cords = findEmpty(board)
    if not cords:
        return True
    else:
        row, col = cords

    for i in range(1, 10):
        if possible(board, row, col, i):
            board[row][col] = i
            if solve(board):
                solution = board
                return True
            board[row][col] = 0
    return False


def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, column
    return None


def pBo(board):
    """Prints given board in readable format"""
    print(mt(board))


# TODO: Decide on UI, How will the program output the data?
def main():
    solve(puzzle)
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    solve(board)
    pBo(board)


if __name__ == "__main__":
    main()
