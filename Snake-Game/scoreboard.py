from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.count}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.count}", align=ALIGNMENT, font=FONT)

    def show_score(self):
        self.count += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over, Final Score: {self.count}", align=ALIGNMENT, font=FONT)






