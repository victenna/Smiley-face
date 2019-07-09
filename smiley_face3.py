import turtle
turtle.tracer(3)
wn=turtle.Screen()
wn.setup(900,900)
wn.bgcolor('orange')

class Face(turtle.Turtle):

    def __init__(self,size):
        self.size = size
               
        super().__init__()
        self.hideturtle()
       
    def draw(self,x,y):
        self.goto(x,y)
        self.pendown()
        self.circle(self.size)
        self.eyes(x,y)
        self.mouth(x,y)
        self.nose(x,y)
        self.hair(x,y)

    def eyes(self,x,y):
        self.up()
        self.goto(x+self.size*2/5,y+self.size*3/2)
        self.pendown()
        self.dot(10)
        self.up()
        self.goto(x-self.size*2/5,y+self.size*3/2)
        self.down()
        self.dot(10)
        
    def mouth(self,x,y):
        self.up()
        self.right(135)
        self.forward(x+self.size/1.7)
        self.left(90)
        self.goto(x-self.size*2/5,y+self.size*4/6.5)
        self.pendown()
        self.circle(self.size/1.7, 90)
        self.setheading(0)

    def nose(self,x,y):
        #self.shapesize(0.2)
        self.up()
        self.goto(x,y+self.size*3/3)
        self.pendown()
        self.color('grey')
        self.dot(self.size/3)
        self.color('black')

    def hair(self,x,y):
        self.up()
        self.pensize(self.size/20)
        for i in range(4):
            self.up()
            self.goto(x,y-20+2*self.size)
            self.setheading(90-10*i)
            self.down()
            self.circle((self.size/2.5),180)
            self.up()
            self.goto(x,y-20+2*self.size)
            self.setheading(90-10*i)
            self.down()
            self.circle(-(self.size/2.5),180)
            self.up()
        self.pensize(1)
        
        
#_________________________________________________ 

X1=-300
Y1=0

for i in range(4):
    #f = Face(70)
    f = Face(75-10*i)
    f.up()
    f.draw(X1,Y1)
    X1=X1+140-20*i





