from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('My snake game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        game_is_on =False
        scoreboard.game_over()

    for i in snake.segments[1:]:
        if snake.segments[0].distance(i) < 15:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
