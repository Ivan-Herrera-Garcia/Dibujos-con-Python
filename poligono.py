import turtle

# Configuración de la ventana de dibujo
window = turtle.Screen()
window.bgcolor("white")

# Crear una instancia de Turtle
t = turtle.Turtle()
t.speed(1)  # Velocidad de dibujo (1 es lento)

# Dibujar un polígono con 6 lados (hexágono)
lados = 6
longitud_lado = 100

for _ in range(lados):
    t.forward(longitud_lado)
    t.left(360 / lados)

# Cierra la ventana al hacer clic en ella
window.exitonclick()
