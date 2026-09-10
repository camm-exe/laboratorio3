import turtle

v = turtle.Screen()
v.setup(width=600, height=400)
t = turtle.Turtle()
t.speed(0)


v.bgcolor("deepskyblue")


t.up()
t.goto(-300, -200)
t.color("limegreen")
t.begin_fill()
for _ in range(2):
    t.forward(600)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()

# Sol
t.goto(-200, 100)
t.color("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()

# Casa
t.goto(50, -50)
t.color("peru")
t.begin_fill()
for _ in range(4):
    t.forward(80)
    t.left(90)
t.end_fill()

# Techo
t.goto(50, 30)
t.color("darkred")
t.begin_fill()
t.goto(90, 80)
t.goto(130, 30)
t.goto(50, 30)
t.end_fill()


t.goto(-100, -50)
t.color("saddlebrown")
t.begin_fill()
for _ in range(2):
    t.forward(15)
    t.left(90)
    t.forward(40)
    t.left(90)
t.end_fill()

t.goto(-110, -10)
t.color("forestgreen")
t.begin_fill()
t.circle(20)
t.end_fill()


t.goto(-180, -150)
t.color("blue")
t.begin_fill()
for _ in range(2):
    t.forward(70)
    t.left(90)
    t.forward(30)
    t.left(90)
t.end_fill()


for rx in [-160, -130]:
    t.goto(rx, -160)
    t.color("black")
    t.begin_fill()
    t.circle(8)
    t.end_fill()

t.hideturtle()
v.exitonclick()
