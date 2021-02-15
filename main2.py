from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your Bet", prompt="Which color of turtle will win the race?:  ")
user_bet = user_bet.lower()
print(f"You bet {user_bet}.")


colors = ['red','orange','yellow','green','blue','purple']
turtles = []

for i in range(0, 6): #0~5, <6
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, -80+40*i)
    turtles.append(new_turtle)

#range는 끝수를 포함하지 않는다. randint는 끝수를 포함한다.)
def race():
    while True:
        for i in turtles:
            r = random.randint(0,10) #0~10, =<10
            i.forward(r)
            if i.xcor()>230:
                if i.pencolor()==user_bet:
                    print(f"You win. {i.pencolor().capitalize()} win")
                else:
                    print(f"You lose. {i.pencolor().capitalize()} win")

                return

race()

screen.exitonclick()