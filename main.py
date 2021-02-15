import turtle

tim=turtle.Turtle()
screen=turtle.Screen()

def move():
    tim.forward(10)

def back():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def reset():
    tim.reset()


screen.listen()
screen.onkey(fun=move, key="w")
screen.onkey(back, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(reset, 'c')

screen.exitonclick()
# turtle.Screen().exitonclick()