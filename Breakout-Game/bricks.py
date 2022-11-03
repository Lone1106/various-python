from turtle import Turtle

positions = [(-320, 260), (-240, 260), (-160, 260), (-80, 260), (0, 260), (80, 260), (160, 260), (240, 260), (320, 260),
             (-320, 230), (-240, 230), (-160, 230), (-80, 230), (0, 230), (80, 230), (160, 230), (240, 230), (320, 230),
             (-320, 200), (-240, 200), (-160, 200), (-80, 200), (0, 200), (80, 200), (160, 200), (240, 200), (320, 200),
             (-320, 170), (-240, 170), (-160, 170), (-80, 170), (0, 170), (80, 170), (160, 170), (240, 170), (320, 170)]
             
all_t = []


class Bricks(Turtle):
    def __init__(self):
        super().__init__()

        self.draw_bricks()


    def draw_bricks(self):
        for pos in positions:
            self.create_brick(pos)


    def create_brick(self, pos):
        new_brick = Turtle("square")
        new_brick.pu()
        new_brick.color("white")
        new_brick.shapesize(stretch_len=3.7, stretch_wid=0.75)
        new_brick.goto(pos)
        all_t.append(new_brick)







        



    


        