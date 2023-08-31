import turtle

# Configuración de la ventana de dibujo
window = turtle.Screen()
window.bgcolor("white")

# Crear una instancia de Turtle
dado = turtle.Turtle()
dado.speed(1)  # Velocidad de dibujo (1 es lento)

# Dibujo del dado
dado.penup()
dado.goto(-50, 50)
dado.pendown()
dado.begin_fill()
for _ in range(4):
    dado.forward(100)
    dado.right(90)
dado.end_fill()

# Dibujar los puntos del dado
dado.penup()
dado.goto(-25, 25)
dado.dot(20, "black")

dado.penup()
dado.goto(-25, -5)
dado.dot(20, "black")

dado.penup()
dado.goto(-25, -35)
dado.dot(20, "black")

dado.penup()
dado.goto(15, 25)
dado.dot(20, "black")

dado.penup()
dado.goto(15, -5)
dado.dot(20, "black")

dado.penup()
dado.goto(15, -35)
dado.dot(20, "black")

# Cierra la ventana al hacer clic en ella
window.exitonclick()
