from turtle import Turtle
ALIGNMENT = "center"
FONT = ("COURIER", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_highscore.txt", mode="r") as highscore_file:
            self.highscore = highscore_file.read()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}     Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("snake_highscore.txt", mode="w") as highscore_file:
                highscore_file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

