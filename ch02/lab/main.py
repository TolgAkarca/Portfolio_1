# Part A 
import random

x = random.randrange(7576467576,9999999999999999)
print(x)




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
tolga.goto(-100,20)
aral.goto(-100,-20)
#Who gonna win

myRange = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50)
for myrange in range(10):
    tolga.forward(random.choice(myRange))
    aral.forward(random.choice(myRange))


screen.exitonclick()



