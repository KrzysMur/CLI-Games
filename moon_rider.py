import os
import time
import random
from pynput import keyboard

class Board:
    def __init__(self):
        self.height = 5
        self.car_offset = 40
        self.ground_length = 50
        self.refresh_delay = 0.05   

    @staticmethod
    def show(car, ground):
        car.show()
        ground.show()



class Car(Board):
    def __init__(self):
        super().__init__()
        self.elevation = 0
        self.symbol = "<&"

    def show(self):
        for _ in range(self.height - self.elevation - 1): print()
        print(" "*self.car_offset + self.symbol)
        for _ in range(self.elevation): print()
    
    def jump(self):
        height = 2
        for _ in range(height):
            self.elevation += 1
            time.sleep(self.refresh_delay*2)
        time.sleep(self.refresh_delay*8)
        for _ in range(height):
            self.elevation -= 1
            time.sleep(self.refresh_delay*2)



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

    def move_holes(self):
        self.holes = [h+1 for h in self.holes if h < self.ground_length]

    def random_generate_hole(self):
        try:
            if self.holes[-1] > random.randint(10, 15) and random.randint(0, 5) == 0:
                self.add_hole()
        except IndexError:
            if random.randint(0, 3): self.add_hole()


def main():

    def on_press(key):
        try:
            if key.name == "space": car.jump(); time.sleep(.2)   
        except AttributeError: pass

    car = Car()
    ground = Ground()

    keyboard.Listener(on_press=on_press).start() 

    running = True
    while running:
        clear()
        Board.show(car, ground)

        ground.random_generate_hole()
        ground.move_holes()     
        time.sleep(car.refresh_delay)






def clear(): 
    os.system("cls")




if __name__ == "__main__":
    main()