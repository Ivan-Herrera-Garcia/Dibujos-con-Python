import tkinter as tk
import time

def actualizar_reloj():
    # Obtén la hora y fecha actual
    ahora = time.localtime()
    hora_actual = time.strftime("%H:%M:%S", ahora)
    dia_semana = time.strftime("%A", ahora)
    dia_mes = time.strftime("%d", ahora)
    mes = time.strftime("%B", ahora)
    año = time.strftime("%Y", ahora)

    # Actualiza la etiqueta con la hora y la fecha completa
    etiqueta.config(text=f"{dia_semana}, {dia_mes} de {mes} de {año} - {hora_actual}")
    
    ventana.after(1000, actualizar_reloj)  # Actualiza cada segundo

# Configura la ventana
ventana = tk.Tk()
ventana.title("Reloj con Fecha y Hora")

# Configura la etiqueta para mostrar la fecha y hora
etiqueta = tk.Label(ventana, text="", font=("Helvetica", 14))
etiqueta.pack(padx=20, pady=20)

from math import pi, cos, sin


# Ventana
root = ventana
root.title("Nos ira bonito 🫶")

# Configuración
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Dibujar el tallo
x0, y0 = 100, 100
x1, y1 = 200, 100
canvas.create_line(x0+100, y0, x1, y1+250, width=10, fill='green')

# Dibujar los pétalos
for i in range(0, 7):
    angle = i * 60 * pi / 180
    x = x1 + 50 * cos(angle)
    y = y1 + 50 * sin(angle)
    canvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill='yellow', outline='white')

# Dibujar el centro
x = x1
y = y1
canvas.create_oval(x - 50, y - 50, x + 50, y + 50, fill='brown')

actualizar_reloj()  # Inicia la actualización del reloj

ventana.mainloop()
