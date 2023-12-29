from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)


food = Food()
snake = Snake()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


while True:
    sleep(0.1)
    screen.update()
    snake.move()

    if snake.collide():
        score.game_over()
        break

    if snake.head.distance(food) < 15:
        food.place()
        snake.extend()
        score.score += 1
        score.write_score()


screen.exitonclick()
