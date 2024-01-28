from turtle import Screen, Turtle


def move_forward():
    t.forward(20)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda")

x = 0
y = 0
for _ in range(0, 3):
    t = Turtle(shape="square")
    t.fillcolor("white")
    t.penup()
    t.teleport(x, y)
    x += 20

game_not_over = True
def running():
    while game_not_over:
        t.forward(20)
        screen.ontimer(running, t=50)














screen.exitonclick()