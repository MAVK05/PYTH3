import turtle
x1 = float(input("enter the center x-coordinate of a circle:"))
y1 = float(input("enter the center y-coordinate of a circle:"))
rad = float(input("enter radius:"))
x2 = float(input("enter a point x-coordinate:"))
y2 = float(input("enter a point y-coordinate:"))

#Draw the circle
turtle.penup()
turtle.goto(x1, y1 - rad)
turtle.pendown()
turtle.circle(rad)

#Draw the point
turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.dot(6, "red")

#draw the status
turtle.penup()
turtle.goto(x1 -70 , y1 - rad -20)
turtle.pendown()

d = ((x2 -x1)**2 + (y2 - y1)**2)**0.5
if (d<=rad):
    turtle.write("The point is inside the circle",font=("Times",12))
else:
    turtle.write("The point is outside the circle", font=("Times",12))
turtle.hideturtle()

turtle.done()                                  
                                  
            
