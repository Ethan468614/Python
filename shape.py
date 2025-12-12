import turtle

turtle.Screen().bgcolor("Red")
turtle.Screen().setup(300,400)
s = turtle.Turtle()

sides = 4

side_len = 80
angle = 360 / sides

for i in range(sides):
    s.forward(side_len)
    s.right(angle)

turtle.done()    