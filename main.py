from turtle import Screen
from snake import Snake
from food import Food
import time
from score import ScoreCard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer()

# Turtle
snake = Snake()
food = Food()
score = ScoreCard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_on = True

while is_game_on:
    count = 0;
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect distance from food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.count_score()

    # Detect collission with wall
    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        is_game_on = False
        score.game_over()

    # Detect collission with tail

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
