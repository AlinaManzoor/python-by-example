import turtle

turtle.color("green" , "pink")
turtle.begin_fill()

for i in range(0,4):
   turtle.forward(100)
   turtle.left(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("green" , "pink")
turtle.begin_fill()

for i in range(0,4):
   turtle.forward(100)
   turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.forward(100)

turtle.pendown()
turtle.color("green" , "pink")
turtle.begin_fill()

for i in range(0,4):
    turtle.forward(100)
    turtle.left(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.exitonclick()