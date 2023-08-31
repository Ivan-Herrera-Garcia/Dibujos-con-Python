import turtle

for x in range(0, 4):
    turtle.forward(50)
    turtle.left(90)
grados = 0
turtle.speed(15)
for x in range(1, 20):
    for x in range(0, 10):
        turtle.forward(50)
        turtle.left(90)
    turtle.left(grados + 10)
turtle.done()
