import turtle

t = turtle.Turtle()

t.color("blue")
for i in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(150, 0)
t.pendown()

t.color("red")
for i in range(4):
    t.forward(80)
    t.right(90)

turtle.done()
