import turtle

# Configurando la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Crear un objeto Turtle
pen = turtle.Turtle()

# Dibujar un rombo
pen.left(45)  # Girar 45 grados a la izquierda
for _ in range(4):
    pen.forward(100)  # Longitud de los lados del rombo
    pen.left(90)      # Girar 90 grados a la izquierda

# Mantener la window abierta hasta que se cerrada manualmente
turtle.done()
