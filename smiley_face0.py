import turtle
wn=turtle.Screen()
t0=turtle.Turtle()
t=turtle.Turtle()
t1=turtle.Turtle('circle')
t1.speed(0)
t2=turtle.Turtle('circle')
t2.speed(0)
def face(x, y,r1,r2,direction,clr):
  t1.penup()
  t1.goto(x,y)
  t1.color(clr)
  t1.shapesize(r1,r2)
  t1.setheading(direction)
  t1.stamp()
  
face(0,0,20,20,0,'red')
face(-60,35,2,2,0,'blue')
face(60,35,2,2,0,'blue')
face(0,10,6,2,0,'grey')
face(0,-120,2,7,0,'green')
#face(0,-110,2,7,0,'green')
face(-245,30,5,5,0,'violet')
face(245,30,5,5,0,'violet')
image0='hat.gif'
image='mustache.gif'
image2='glasses.gif'
wn.addshape(image0)
wn.addshape(image)
wn.addshape(image2)
t0.shape(image0)
t0.goto(0,205)
t.shape(image)
t.goto(0,-70)
t2.shape(image2)
t2.goto(0,30)


