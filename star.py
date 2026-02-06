import turtle

turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(500,700)
pen = turtle.Turtle()

#1st Triangle
pen.forward(100)

pen.left(120)
pen.forward(100)

pen.left(120)
pen.forward(100)

pen.penup()
pen.right(150)
pen.forward(50)

#2nd Triangle

pen.pendown()
pen.right(90)
pen.forward(100)

pen.right(120)
pen.forward(100)

pen.right(120)
pen.forward(100)

pen.done()