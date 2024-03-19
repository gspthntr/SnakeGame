from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

current_score = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")

game_not_over = True
while game_not_over:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.out_of_bounds() or snake.collision():
        scoreboard.reset()
        snake.snake_reset()
        screen.update()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.new_segment()
        scoreboard.increase_score()

screen.exitonclick()
