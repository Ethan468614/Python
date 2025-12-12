import turtle
turtle.bgcolor("Blue")
turtle.Screen().setup(300,400)
t = turtle.Turtle()




sides = 3
side_len = 80
angle = 360 / sides

for i in range(sides):
    t.forward(side_len)
    t.left(angle)

turtle.done()
