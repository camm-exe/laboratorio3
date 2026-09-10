import turtle

v = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")


t.pensize(5)
colores = ["green", "orange", "red", "blue"]

for color in colores:
    t.color(color)
    t.down()
    t.forward(80)
    t.up()
    t.forward(20)
    t.right(90)

v.exitonclick()



