import turtle 



turtle.screensize(720,420)
screen = turtle.Screen()
screen.bgcolor('red')
pen = turtle.Turtle()
screen.title('Turkey is now 100 years old ')

def circle1() :
    pen.color('white')
    pen.up()
    pen.goto(-180,-100)
    pen.down()
    pen.begin_fill()
    pen.circle(180)
    pen.end_fill()

def circle2() :
    pen.color('red')
    pen.up()
    pen.goto(-120,-80)
    pen.down()
    pen.begin_fill()
    pen.circle(160)
    pen.end_fill()


def star() :
    
    pen.color('white')
    pen.up()
    pen.goto(10,100)
    pen.down()
    pen.begin_fill()
    for _ in range(5):
        
        pen.forward(75)
        pen.right(144)
        pen.forward(75)
        pen.right(-72)
    pen.end_fill()   
    
    return pen.xcor(), pen.ycor()



    
circle1()
circle2()
x, y = star()
print(f"The pen is at coordinates ({x}, {y}) after drawing the star.")
print('Flag is completed !!!')
screen.exitonclick()