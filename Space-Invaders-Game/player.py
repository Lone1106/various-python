from turtle import Turtle

##########

MOVE_INCREMENT = 15

##########

class Player(Turtle):
    def __init__(self, position, rotation):
        super().__init__()

        self.shape("triangle")
        self.color("red")
        self.pu()
        self.goto(position)
        self.left(rotation)

        self.all_shots = []
        self.move_y = 10



    def move_right(self):
        new_x = self.xcor() + MOVE_INCREMENT
        self.goto(new_x, self.ycor())


    def move_left(self):
        new_x = self.xcor() +  -MOVE_INCREMENT
        self.goto(new_x, self.ycor())

    
    def stop_moving(self, position):
        self.goto(position, self.ycor())


    def create_shot(self):
        #Only 1 shot at a time
        if len(self.all_shots) == 0:
            new_shot = Turtle()
            new_shot.color("red")
            new_shot.pu()
            new_shot.shape("square")
            new_shot.shapesize(stretch_wid=0.25, stretch_len=1)
            new_shot.left(90)
            new_shot.goto(self.xcor(), self.ycor())
            self.all_shots.append(new_shot)





 



