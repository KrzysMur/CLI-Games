import os
import time
import random

class Board:
    def __init__(self):
        self.height = 5
        self.car_offset = 40
        self.ground_length = 50



class Car(Board):
    def __init__(self):
        super().__init__()
        self.elevation = 0
        self.symbol = "o-=O"

    def show(self):
        for _ in range(self.height - self.elevation - 1): print()
        print(" "*self.car_offset + self.symbol)
        for _ in range(self.elevation): print()
    



class Ground(Board):
    def __init__(self):
        super().__init__()
        self.holes = [0]
        self.symbol = "#"

    def show(self):
        ground = self.symbol * self.ground_length
        for h in self.holes:
            ground = ground[:h] + " " + ground[h+1:]
        print(ground)

    def add_hole(self):
        self.holes.append(0)



def show_board(car, ground):
    car.show()
    ground.show()

def clear(): 
    os.system("cls")

def move_holes(ground):
    ground.holes = [h+1 for h in ground.holes if h < ground.ground_length]

def main():
    car = Car()
    ground = Ground()

    running = True
    while running:
        clear()
        show_board(car, ground)

        if ground.holes[-1] > random.randint(10, 15) and random.randint(0, 5) == 0:
            ground.add_hole()


        move_holes(ground)
        time.sleep(.01)

if __name__ == "__main__":
    main()