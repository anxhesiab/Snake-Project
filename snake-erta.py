#kodi do te hidhet sipas nr rendor
import turtle
import time
from random import randrange
delay= 0.2
#  1
# Set up the screen
snake= turtle.Screen()
snake.title("Snake Game")
snake.bgcolor("Blue")
snake.setup(width=600, height=600)
snake.tracer(0)  # Turns off the screen updates

# 2
# Snake Head
snake_head= turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("black")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction= "stop"

# 3
# Snake apple
apple= turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0, 100)
segments= []

# 4
# score
score = 0
highest_score = 0
text = turtle.Turtle()
text.speed(0)
text.shape("square")
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Score: 0 High Score: {}".format(highest_score), align="center", font=("Courier", 24, "normal"))


# 5
# Functions
def moving():
    if snake_head.direction == "up":
        y = snake_head.ycor() #y coordinate of the turtle
        snake_head.sety(y + 20)
 
    if snake_head.direction == "down":
        y = snake_head.ycor() #y coordinate of the turtle
        snake_head.sety(y - 20)
 
    if snake_head.direction == "right":
        x = snake_head.xcor() #y coordinate of the turtle
        snake_head.setx(x + 20)
 
    if snake_head.direction == "left":
        x = snake_head.xcor() #y coordinate of the turtle
        snake_head.setx(x - 20)


# 6

# Keyboard Bindings
def up():
    if snake_head.direction != "down":
        snake_head.direction = "up"
 
def down():
    if snake_head.direction != "up":
        snake_head.direction = "down"
 
def right():
    if snake_head.direction != "left":
        snake_head.direction = "right"
 
def left():
    if snake_head.direction != "right":
        snake_head.direction = "left"
 # 7
snake.listen()
snake.onkey(up, "w")
snake.onkey(down, "s")
snake.onkey(right, "d")
snake.onkey(left, "a")

# 8
# Main game loop
while True:
    snake.update()
    time.sleep(delay)

    # 9 
    # moving the apple to a random position on screen
    if snake_head.distance(apple) < 15:
      x = randrange(-290, 290)
      y = randrange(-290, 290)
      apple.goto(x, y)

      # 16
      # Increase the score
      score = score+10
      if score > highest_score:
        highest_score = score
      #segments = []
      text.clear()
      text.write("Score: {} High Score: {}".format(score, highest_score), align="center", font=("Courier", 24, "normal"))

    # 10
    # add a segment
      segment = turtle.Turtle()
      segment.speed(0)
      segment.shape("square")
      segment.color("grey")
      segment.penup()
      segments.append(segment)

    # 11
    # moving the end segment in reverse order
    for index in range(len(segments)-1, 0, -1):
      x = segments[index-1].xcor()
      y = segments[index-1].ycor()
      segments[index].goto(x, y)

    # 12
    # Move segment 0 to where the snake_head is
    if len(segments)>0:
      x = snake_head.xcor()
      y = snake_head.ycor()
      segments[0].goto(x, y)

    moving()

    # 13
    # Check for collision
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
      time.sleep(1)
      snake_head.goto(0, 0)
      snake_head.direction = "stop"

      # 14
      # Hide the segments
      for segment in segments:
        segment.goto(1000, 1000) 
      # clear segment list
      segments = []

        # 17
      # reset score
      score = 0
      # update score
      text.clear()
      text.write("score: {} High Score: {}".format(score, highest_score), align="center", font=("Courier", 24, "normal"))

    # 15
    # Check for snake_head collision
    for segment in segments:
      if segment.distance(snake_head) < 20:
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"
    # Hide the segments
        for segment in segments:
          segment.goto(1000, 1000)
          #clear segment list
        segments.clear()
        # reset score
        score = 0
        # update score
        text.clear()
        text.write("score: {} High Score: {}".format(score, highest_score), align="center", font=("Courier", 24, "normal"))

    