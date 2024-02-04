import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food = Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() <= 280 and snake.head.xcor() >= -280 and snake.head.ycor() <= 280 and snake.head.ycor() >= -280:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    #slicing
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


        











screen.exitonclick()