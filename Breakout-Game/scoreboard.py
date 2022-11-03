from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGN = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.pu()
        self.hideturtle()
        self.score_count = 0
        self.level = 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(0,275)
        self.write(f"Level: {self.level} Score: {self.score_count}", align=ALIGN, font=FONT)


    def add_point(self):
        self.score_count += 1
        self.update_scoreboard()

    
    def game_over(self):
        self.goto(0, 0)
        self.score_count = 0
        self.write("GAME OVER", align=ALIGN, font=FONT)
