import turtle as t
import random

# Configuración inicial
t.speed(0)
t.bgcolor("white")
t.title("Dibujo de una flor")
t.setup(500, 500, -500, -500)

# Función para dibujar un pétalo
def draw_petal(color, radius, angle):
    t.penup()
    t.fillcolor(color)
    t.left(angle)
    t.forward(radius)
    t.pendown()
    t.begin_fill()
    t.circle(10, 180)
    t.left(90)
    t.circle(10, 180)
    t.end_fill()
    t.right(angle)
    t.penup()
    t.backward(radius)
    t.pendown()

# Dibujar la flor
colors = ["red", "orange", "yellow", "pink", "purple"]

for _ in range(12):
    random_color = random.choice(colors)
    draw_petal(random_color, 30, 60)
   

    t.left(360 / 12)

# Dibujar el tallo
t.penup()
t.goto(-30, 5)
t.pendown()
t.color("green")
t.pensize(5)
t.goto(-30, -100)

# Dibujar el tallo
t.penup()
t.goto(10, -15)
t.pendown()
t.color("green")
t.pensize(5)
t.goto(10, -100)

# Dibujar el tallo
t.penup()
t.goto(-2, 40)
t.pendown()
t.color("green")
t.pensize(5)
t.goto(-2, -100)

t.penup()
t.goto(-1000, -100)
t.pendown()
t.color("brown")
t.pensize(5)
t.goto(1000, -100)


# Ocultar la tortuga y mostrar el dibujo
t.hideturtle()
t.done()
