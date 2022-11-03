from turtle import Turtle
import random

##########

positions = [
    (-200, 240), (-160, 240), (-120, 240), (-80, 240), (-40, 240), (0, 240), (40, 240), (80, 240), (120, 240), (160, 240), (200, 240),
    (-200, 200), (-160, 200), (-120, 200), (-80, 200), (-40, 200), (0, 200), (40, 200), (80, 200), (120, 200), (160, 200), (200, 200),
    (-200, 160), (-160, 160), (-120, 160), (-80, 160), (-40, 160), (0, 160), (40, 160), (80, 160), (120, 160), (160, 160), (200, 160)
    ]

##########

class Enemies(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = -7
        self.all_enemies = []
        self.all_shots = []
        self.spawn_enemies()

    
    def spawn_enemies(self):
        for pos in positions:
            self.create_enemy(pos)


    def create_enemy(self, position):
        new_enemy = Turtle()
        new_enemy.pu()
        new_enemy.shape("circle")
        new_enemy.color("green")
        new_enemy.goto(position)
        
        self.all_enemies.append(new_enemy)


    def move(self):
        for enemy in self.all_enemies:
            enemy.back(self.x_move)


    def bounce_left(self):
        self.x_move == 7

    
    def bounce_right(self):
        self.x_move *= -1


    def shoot(self):
        for enemy in self.all_enemies:
            random_chance = random.randint(1, 500)
            if random_chance == 1:
                self.create_shot((enemy.xcor(), enemy.ycor()))



    def create_shot(self, position):
        new_shot = Turtle()
        new_shot.color("green")
        new_shot.pu()
        new_shot.shape("square")
        new_shot.shapesize(stretch_wid=0.25, stretch_len=1)
        new_shot.left(90)
        new_shot.goto(position)

        self.all_shots.append(new_shot)



