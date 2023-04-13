import random
import os
import time

class Board(object):
    def __init__(self):
        self.board = None
        self.mines = 0

    def generate_random(self):
        self.board = [[random.randint(0, 1) for _ in range(5)] for _ in range(5)]
        for row in self.board: self.mines += row.count(1)

    def count_neighbouring_ones(self, square):
        counter = 0
        end_y = len(self.board)-1
        end_x = len(self.board[0])-1
        if square[0] > 0:
            if self.board[square[0]-1][square[1]] == 1: counter += 1
            if square[1] > 0 and self.board[square[0]-1][square[1]-1] == 1: counter += 1
            if square[1] < end_x and self.board[square[0]-1][square[1]+1] == 1: counter += 1
        if square[1] > 0 and self.board[square[0]][square[1]-1] == 1: counter += 1
        if square[1] < end_x and self.board[square[0]][square[1]+1] == 1: counter += 1
        if square[0] < end_y:
            if self.board[square[0]+1][square[1]] == 1: counter += 1
            if square[1] > 0 and self.board[square[0]+1][square[1]-1] == 1: counter += 1
            if square[1] < end_x and self.board[square[0]+1][square[1]+1] == 1: counter += 1
        return counter


class UserBoard(Board):

    def __init__(self, board):
        super().__init__()
        self.board = board.board
        self.mines = board.mines
        self.usr_board = ["# # # # #"] * 5
        self.marked = 0

    def show(self):
        print("   A B C D E        marks left:", self.mines - self.marked)
        for i, row in enumerate(self.usr_board): print(f"{i+1}  {row}")

    def uncover_square(self, square):
        if self.board[square[0]][square[1]] == 0:
            if self.usr_board[square[0]][square[1]*2] == "X": self.marked -=1
            neighbours = self.count_neighbouring_ones(square)
            self.usr_board[square[0]] = self.usr_board[square[0]][:square[1]*2] + str(neighbours) + self.usr_board[square[0]][square[1]*2+1:]
            return True
        else:
            print("YOU DIED...")
            return False

    def mark_square(self, square):
        if self.marked < self.mines:
            self.marked += 1
            self.usr_board[square[0]] = self.usr_board[square[0]][:square[1]*2] + "X" + self.usr_board[square[0]][square[1]*2+1:]
        else: print("No more marks left...")

class InputParser:
    def __init__(self):
        self.usr_input = ""
        self.parsed = None

    def get_input(self):
        self.usr_input = input(">> ")

    def parse_square(self):
        try:
            self.usr_input = self.usr_input.replace(" ", "").upper()
            letter_num = ord(self.usr_input[-2])
            self.parsed = (int(self.usr_input[-1])-1, letter_num-65, self.usr_input[0] == "M")
        except Exception: self.get_input(); self.parse_square()


def main():
    board = Board()
    board.generate_random()
    usr_board = UserBoard(board)
    input_parser = InputParser()
    print(f"Mines on the board: {board.mines}")
    time.sleep(1)

    running = True

    while running:
        #os.system("cls")
        usr_board.show()
        input_parser.get_input()
        input_parser.parse_square()
        square = input_parser.parsed
        if not square[2]: running = usr_board.uncover_square(square)
        else: usr_board.mark_square(square)




if __name__=="__main__":
    main()