import turtle

# Configurando la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Crear un objecto Turtle
pen = turtle.Turtle()

# Dibujar un pentágono
for _ in range(5):
    pen.forward(100)  # Longitud del lado del pentágono
    pen.right(72)     # Ángulo entre los lados del pentágono

# Mantener la ventana abierta hasta que se cierre manualmente
turtle.done()
