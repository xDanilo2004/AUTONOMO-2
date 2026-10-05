import tkinter as tk
from tkinter import messagebox
import random

def jugar(eleccion_jugador):
   
    opciones = ["Piedra", "Papel", "Tijera"]
    eleccion_pc = random.choice(opciones)

    if eleccion_jugador == eleccion_pc:
        resultado = "Empate"
   
    elif (eleccion_jugador == "Piedra" and eleccion_pc == "Tijera") or \
         (eleccion_jugador == "Papel" and eleccion_pc == "Piedra") or \
         (eleccion_jugador == "Tijera" and eleccion_pc == "Papel"):
        resultado = "Gana el jugador"
    else:
        resultado = "Gana la PC"

    messagebox.showinfo("Resultado", f"Jugador eligio: {eleccion_jugador}\nLa PC eligio: {eleccion_pc}\n\n{resultado}")

root = tk.Tk()
root.title("Piedra, Papel o Tijera")
root.geometry("400x200")


tk.Label(root, text="Elige tu opcion: ").grid(row=0, column=0, columnspan=3)

btn_piedra = tk.Button(root, text="Piedra", width=10, command=lambda: jugar("Piedra"))
btn_piedra.grid(row=1, column=0, padx=10, pady=20)

btn_papel = tk.Button(root, text="Papel", width=10, command=lambda: jugar("Papel"))
btn_papel.grid(row=1, column=1, padx=10, pady=20)

btn_tijera = tk.Button(root, text="Tijera", width=10, command=lambda: jugar("Tijera"))
btn_tijera.grid(row=1, column=2, padx=10, pady=20)

root.mainloop()