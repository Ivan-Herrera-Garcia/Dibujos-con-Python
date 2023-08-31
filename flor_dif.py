import turtle

# Configuración inicial de la turtle
t = turtle.Turtle()
t.speed(0)  # Velocidad máxima

# Función para dibujar un pétalo
def dibujar_petalo():
    t.color("yellow")
    t.begin_fill()
    t.circle(50, 60)  # Dibuja un arco de 60 grados con radio 50
    t.left(120)
    t.circle(50, 60)
    t.end_fill()

# Función para dibujar una flor
def dibujar_flor():
    for _ in range(6):  # Dibuja 6 pétalos
        dibujar_petalo()
        t.left(60)  # Gira 60 grados para el siguiente pétalo

# Dibuja la flor en el centro de la ventana
t.penup()
t.goto(0, -50)
t.pendown()
dibujar_flor()

# Dibujar el tallo
t.penup()
t.goto(0, -100)
t.pendown()
t.color("green")
t.pensize(5)
t.goto(0, -200)


# Cierra la ventana al hacer clic en ella
turtle.exitonclick()
