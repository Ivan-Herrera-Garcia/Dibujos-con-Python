import turtle

# Configurando la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Crear un objeto Turtle
pen = turtle.Turtle()

# Dibujar un triángulo equilátero
for _ in range(3):
    pen.forward(100)  # Longitud del lado del triángulo
    pen.left(120)     # Giro de 120 grados a la izquierda

# Mantener la ventana abierta hasta que se cerrada manualmente
turtle.done()
