from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = int(5)
MOVE_INCREMENT = int(10)
cars_on_star_pos = []
cars_moving = []
NUMBER_OF_CARS = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

        for i in range(NUMBER_OF_CARS):
            for copy in COLORS:
                self.car = Turtle()
                self.car.shape("square")
                self.car.shapesize(stretch_wid=1, stretch_len=2)
                self.car.penup()
                self.car.color(copy)
                self.car.setposition(x=320, y=random.randint(-260, 260))
                cars_on_star_pos.append(self.car)

    def change_status(self):
        if len(cars_on_star_pos)-1 != -1:
            random_number = random.randint(0, len(cars_on_star_pos)-1)
            cars_moving.append(cars_on_star_pos[random_number])
            cars_on_star_pos.pop(random_number)

    def change_back_status(self, car_index):
        cars_moving[car_index].setposition(x=320, y=random.randint(-250, 250))
        cars_on_star_pos.append(cars_moving[car_index])
        cars_moving.pop(car_index)

    def start_game(self, level):
        self.moving(level=level)
        self.end_of_the_road()
        percentage_chance = level * 0.15
        if random.random() < percentage_chance:
            self.change_status()

    def moving(self, level):
        for n in cars_moving:
            n.back(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level-1))

    def end_of_the_road(self):
        for i in cars_moving:
            if i.xcor() < -320:
                car_index = cars_moving.index(i)
                self.change_back_status(car_index)

