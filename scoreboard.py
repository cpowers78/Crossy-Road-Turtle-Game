from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 1
        self.goto(-245,270)

    def update_score(self):
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="YOU LOST. GAME OVER.", align=ALIGNMENT, font=FONT)


