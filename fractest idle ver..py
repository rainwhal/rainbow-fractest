import turtle 

wn = turtle.Screen()
wn.colormode(255) # so as to randomly assign colors to different branches of the fractal tree
wn.title('Recursive Circles!') # give the title to the window
turtle.Turtle()
wn.setup(1200, 1200)
wn.bgcolor('black') # for aesthetics
wn.setup(1200, 1200) # set the screen size


def drawCircle(turtle, x, y, radius):
   turtle.penup()
   turtle.setposition(x, y)
   turtle.pendown()
   turtle.circle(radius)

   if radius > 8:
      drawCircle(turtle, x + radius, y + radius / 2, radius / 2)
      drawCircle(turtle, x - radius, y + radius / 2, radius / 2)
      drawCircle(turtle, x, y - radius / 2, radius / 2)
      drawCircle(turtle, x, y + 3 *radius / 2, radius / 2)

   else :
      return


turtle.pencolor('white')
turtle.speed(0)
turtle.right(90)
radius = 200
turtle.penup()
turtle.forward(radius)
turtle.pendown()
turtle.left(90)

drawCircle(turtle, turtle.position()[0],  turtle.position()[1], radius)

wn.exitonclick()
