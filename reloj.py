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

actualizar_reloj()  # Inicia la actualización del reloj

ventana.mainloop()
