import turtle

# Create object
t = turtle.Turtle()

##############
## Settings ##
##############
'''
# Title
turtle.title("This is the title!")

# Turtle shape ( "turtle" , "circle", "arrow" )
t.shape("turtle")

# Increase the turtle size (width, length, arrow size)
t.shapesize(3, 3, 3)

# background color
turtle.bgcolor("yellow")

# Change line size
t.pensize(4)

# Turtle color
t.fillcolor("blue")

# Line color
t.pencolor("red")

# Line color
t.color("red")
'''

##############
## Movement ##
##############
'''
# Move forward + distance
t.fd(100)

# Turn right + degrees
t.rt(90)

# Move back + distance
t.bk(100)

# Turn left + degrees
t.lt(90)
'''

############
## Circle ##
############
'''
# Circle (radius, how much of the circle to draw, time to draw
t.circle(100)

# dot (size, color)
t.dot(50, "blue")
'''

# Keep screen open
turtle.mainloop()



#############
## Example ##
#############

'''
import turtle

# Creating turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("red")

a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
while (True):
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    t.hideturtle()

turtle.done()
'''