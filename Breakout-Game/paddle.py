from turtle import Turtle

MOVE_INCREMENT = 35

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.pu()
        self.shapesize(stretch_len=8, stretch_wid=0.3)
        self.goto(position)

    
    def go_right(self):
        new_x = self.xcor() + MOVE_INCREMENT
        self.goto(new_x, self.ycor())


    def go_left(self):
        new_x = self.xcor() + -MOVE_INCREMENT
        self.goto(new_x, self.ycor())