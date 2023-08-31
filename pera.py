import turtle

# Configuración inicial
turtle.speed(1)
turtle.bgcolor("white")
turtle.color("green")
turtle.pensize(2)

# Dibujo del cuerpo
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# Cabeza
turtle.penup()
turtle.goto(0, 60)
turtle.pendown()
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# Antena
turtle.penup()
turtle.goto(0, 120)
turtle.pendown()
turtle.forward(10)
turtle.circle(5)

# Ojos
turtle.penup()
turtle.goto(-20, 75)
turtle.pendown()
turtle.dot(10)

turtle.penup()
turtle.goto(20, 75)
turtle.pendown()
turtle.dot(10)

# Boca
turtle.penup()
turtle.goto(-25, 50)
turtle.pendown()
turtle.right(90)
turtle.circle(25, 180)

# Terminar
turtle.hideturtle()
turtle.done()
