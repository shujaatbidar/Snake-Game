from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.listen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(False)
snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score.show_score()
        food.refresh()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            score.game_over()

screen.exitonclick()

