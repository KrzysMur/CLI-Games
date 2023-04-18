import os


class Board:
    def __init__(self):
        self.y_offset = 4
        self.car_offset = 40
        self.ground_length = 50

class Car(Board):
    def __init__(self):
        super().__init__()
        self.elevation = 0
        self.symbol = "o-=O"

    def show(self):
        print(" "*self.car_offset + self.symbol)
    



class Ground(Board):
    def __init__(self):
        super().__init__()
        self.holes = []
        self.symbol = "#"

    def show(self):
        ground = self.symbol * self.ground_length
        for h in self.holes:
            ground = ground[:h] + " " + ground[h+1:]
        print(ground)




def main():
    car = Car()
    ground = Ground()

    car.show()
    ground.show()


if __name__ == "__main__":
    main()