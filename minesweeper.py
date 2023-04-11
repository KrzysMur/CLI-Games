import random
import os

class Board(object):
    def __init__(self):
        self.board = [[1, 1, 0, 1, 0], [0, 0, 0, 1, 1], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1], [1, 1, 0 ,0, 0]]

    def generate_random(self):
        return [[random.randint(0, 1) for j in range(5)] for i in range(5)]

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

    def __init__(self):
        super().__init__()
        self.usr_board = ["# # # # #"] * 5

    def show(self):
        print("   A B C D E")
        for i, row in enumerate(self.usr_board): print(f"{i+1}  {row}")

    def uncover_square(self, square):
        if self.board[square[0]][square[1]] == 0:
            neighbours = self.count_neighbouring_ones(square)
            self.usr_board[square[0]] = self.usr_board[square[0]][:square[1]*2] + str(neighbours) + self.usr_board[square[0]][square[1]*2+1:]
            return True
        else:
            print("YOU DIED...")
            return False

    def mark_square(self, square):
        self.usr_board[square[0]] = self.usr_board[square[0]][:square[1]*2] + "X" + self.usr_board[square[0]][square[1]*2+1:]


class InputParser:
    def __init__(self):
        self.usr_input = ""
    
    def get_input(self):
        self.usr_input = input(">> ")

    def parse_square(self):

        self.usr_input = self.usr_input.replace(" ", "").upper()
        letter_num = ord(self.usr_input[-2])
        return (int(self.usr_input[-1])-1, letter_num-65, self.usr_input[0] == "M")



def main():
    board = Board()
    usr_board = UserBoard()
    input_parser = InputParser()
    
    running = True

    while running:
        os.system("cls")
        usr_board.show()
        input_parser.get_input()
        square = input_parser.parse_square()
        if not square[2]: running = usr_board.uncover_square(square)
        else: usr_board.mark_square(square)




if __name__=="__main__":
    main()