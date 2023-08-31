import turtle

# Configurando la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Crear un objeto Turtle
pen = turtle.Turtle()

# Dibujar un cuadrado
for _ in range(4):
    pen.forward(100)  # Longitud del lado del cuadrado
    pen.left(90)      # Giro de 90 grados a la izquierda

# Mantener la ventana abierta hasta que se cierre manualmente
turtle.done()
