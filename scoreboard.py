from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def up(self):
        self.level += 1
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Level: {self.level}", align="center", font=FONT)
        self.goto(0, 50)
        self.write("GAME OVER", align="center", font=FONT)
