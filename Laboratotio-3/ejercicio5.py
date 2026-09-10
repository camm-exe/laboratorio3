import turtle

v = turtle.Screen()
t = turtle.Turtle()


def dibujar_figura(x, y, lados, tam, color, angulo_inicio=0):
    t.up()
    t.goto(x, y)
    t.setheading(angulo_inicio)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(lados):
        t.forward(tam)
        t.left(360 / lados)
    t.end_fill()


dibujar_figura(-180, 50, 3, 60, "deepskyblue")  
dibujar_figura(-80, 50, 4, 60, "red")  

t.up()
t.goto(20, 50)
t.down()
t.fillcolor("yellow")
t.begin_fill()
for _ in range(2):
    t.forward(80)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()


t.up()
t.goto(150, 50)
t.down()
t.fillcolor("limegreen")
t.begin_fill()
t.circle(30)
t.end_fill()


dibujar_figura(-180, -100, 4, 50, "yellow", 45)  

t.up()
t.goto(-80, -100)
t.down()
t.fillcolor("deepskyblue")
t.begin_fill()
for _ in range(2):
    t.forward(60)
    t.left(60)
    t.forward(50)
    t.left(120)
t.end_fill()


t.up()
t.goto(20, -100)
t.down()
t.fillcolor("limegreen")
t.begin_fill()
t.forward(60)
t.left(110)
t.forward(50)
t.left(70)
t.forward(94.2)
t.left(70)
t.forward(50)
t.end_fill()

t.up()
t.goto(150, -80)
t.down()
t.fillcolor("red")
t.begin_fill()
t.setheading(45)
for _ in range(2):
    t.circle(40, 90)
    t.circle(20, 90)
t.end_fill()

v.exitonclick()
