import turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t = turtle.Turtle()
t.speed(10)

for i in range(60):
    t.color(colors[i % 6])
    t.forward(i * 3)
    t.right(60)

turtle.done()
