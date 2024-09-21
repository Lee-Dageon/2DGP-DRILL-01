import turtle
turtle.shape('turtle')

def move_up():
        turtle.setheading(90)
        turtle.forward(50)
        turtle.stamp()
def move_left():
        turtle.setheading(180)
        turtle.forward(50)
        turtle.stamp()
def move_down():
        turtle.setheading(270)
        turtle.forward(50)
        turtle.stamp()
def move_right():
        turtle.setheading(0)
        turtle.forward(50)
        turtle.stamp()

def game_restart():
    turtle.goto(0,0)
    turtle.clear()

    
turtle.listen()
turtle.onkey(move_up, 'w')   
turtle.onkey(move_up, 'W')   
turtle.onkey(move_left, 'a') 
turtle.onkey(move_left, 'A') 
turtle.onkey(move_down, 's') 
turtle.onkey(move_down, 'S') 
turtle.onkey(move_right, 'd') 
turtle.onkey(move_right, 'D')
turtle.onkey(game_restart, 'Escape')

turtle.exitonclick()



