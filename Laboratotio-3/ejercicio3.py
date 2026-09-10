import math
import turtle

v = turtle.Screen()
v.title("Ejercicio 3: Círculo y Área")

x = v.numinput("Centro", "Coordenada X del centro:", default=0)
y = v.numinput("Centro", "Coordenada Y del centro:", default=0)
radio = v.numinput("Radio", "Ingrese el radio del círculo:", default=50, minval=1)

area = math.pi * (radio**2)

t = turtle.Turtle()
t.hideturtle()
t.speed(3)

t.up()
t.goto(x, y - radio)
t.down()
t.color("red")
t.circle(radio)

t.up()
t.goto(x, y - 5)  
t.color("blue")
t.write(f"{area:.2f}", align="center", font=("Arial", 10, "bold"))

v.exitonclick()
