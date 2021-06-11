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
 
snake.listen()
snake.onkey(up, "w")
snake.onkey(down, "s")
snake.onkey(right, "d")
snake.onkey(left, "a")
