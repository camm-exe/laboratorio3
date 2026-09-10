import turtle

v=turtle.Screen()
v.bgcolor('yellow')

t=turtle.Turtle()
t.color('green')
t.pensize(10)

t.left(90)
t.forward(100)
t.right(150)
t.forward(115)
t.left(150)
t.forward(100)

t.up()
t.home()
t.forward(150)
t.down()
t.backward(50)
t.left(90)
t.forward(100)

v.exitonclick()
