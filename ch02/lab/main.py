# Part A 
import random

x = random.randrange(7576467576,9999999999999999)
print(x)


#Part B

import turtle  # 1. import modules
import random

screen = turtle.Screen()
#create and name turtles 
tolga = turtle.Turtle()
aral = turtle.Turtle()
#color of the turtles
tolga.color("cyan")
aral.color("brown")
#shape of the turtles
tolga.shape("turtle")
aral.shape("turtle")
#starting point of turtles
tolga.up()  
aral.up()
tolga.goto(-100,-20)
aral.goto(-100,20)
#Who gonna win
myRange = (90,200,120,100,50,20,10,70,67,32,87,45,97,148,216)
aral.forward(random.choice(myRange))
tolga.forward(random.choice(myRange))


screen.exitonclick()


