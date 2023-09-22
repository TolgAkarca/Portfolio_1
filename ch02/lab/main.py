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



#Part B
import math 
import pygame
pygame.init()
window = pygame.display.set_mode()
while True:
    for event in pygame.event.get():
        pass
    window = pygame.display.set_mode()
    shapes = [3,4,6,20,100,360]
    for num_sides in shapes :

        side_lenght = 50
        xpos = 300
        ypos = 300
        points = []
        for i in range(num_sides):
            angle = 360/num_sides
            radians = math.radians(angle * i)
            x = xpos + side_lenght * math.cos(radians)
            y = ypos + side_lenght * math.sin(radians)
            points.append([x,y])
     
        pygame.draw.polygon(window, 'red', points)
        pygame.display.flip()
        window.fill('black')
        pygame.display.flip
        pygame.time.wait(300)

