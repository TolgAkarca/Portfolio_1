import turtle       


sides = int(input("Please enter  the number of sides:\n" ))
sidesLenght = int(input("Please enter lenght of each sides(recommended 75)\n "))
angle =  360 / sides
screen = turtle.Screen()
screen.screensize(1000,1000)
tolga = turtle.Turtle()
tolga.color('cyan')
tolga.shape('turtle')
for x in range(sides):
    tolga.forward(sidesLenght)
    tolga.left(angle)



screen.exitonclick()
