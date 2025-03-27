import turtle

turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,500)

side=4
angle=360/side

square=turtle.Turtle()
for i in range(side):
    square.forward(100)
    square.right(angle)
turtle.done()