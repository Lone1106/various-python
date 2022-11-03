from turtle import Turtle

##########

ALIGN = "center"
FONT = ("Courier", 20, "normal")

##########

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("white")
        self.pu()
        self.hideturtle()
        self.update_scoreboard()
    

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Current Score: {self.score}", align=ALIGN, font=FONT)

    
    def add_point(self):
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER! Score: {self.score}", font=FONT, align=ALIGN)
        self.score = 0


    def game_won(self):
        self.clear()
        self.goto()
        self.write(f"You won! Score: {self.score}", align=ALIGN, font=FONT)



