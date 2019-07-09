import turtle
t=turtle.Turtle()
turtle.bgcolor('gold')
t.hideturtle()
turtle.tracer(2)

t.penup()
t.goto(0,-150)
t.color('red')
t.begin_fill()
t.pendown()
t.circle(150)
t.penup()
t.end_fill()
t.left(180)

def triangle(x, y, clr):
  t.penup()
  t.goto(x,y)
  t.begin_fill()
  t.color(clr)
  t.pendown()
  for j in range(3):
    t.fd(50)
    t.lt(120)
  t.end_fill()

def square(x, y, clr):
  t.penup()
  t.goto(x,y)
  t.begin_fill()
  t.color(clr)
  t.pendown()
  for i in range(3):
    t.fd(50)
    t.lt(90)
  t.end_fill()

triangle(-30, -40, '#ffffff')
triangle(5, -40, '#ffffff')
triangle(40, -40, '#ffffff')
#t.left(180)

triangle(-70, 50, '#ffffff')
triangle(80, 50, '#ffffff')



