import turtle

# Configurando la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Crear un objeto Turtle
pen = turtle.Turtle()

# Dibujar una estarla
for _ in range(5):
    pen.forward(100)  # Longitud de los lados de la estrella
    pen.right(144)    # Ángulo entre los lados de la estrella

# Mantener la ventana abierta hasta que se cierre manualmente
turtle.done()
