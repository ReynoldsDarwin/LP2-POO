import tkinter as tk
from tkinter import messagebox

class Fibonacci:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.serie = []

    def generarSerie(self):
        a, b = 0, 1
        for _ in range(self.cantidad):
            self.serie.append(a)
            a, b = b, a + b
        return self.serie


def calcular_fibonacci():
    try:
        cantidad = int(entry.get())
        if cantidad < 0:
            messagebox.showerror("Error", "Ingrese un número positivo")
            return
        miFibonacci = Fibonacci(cantidad)
        resultado = miFibonacci.generarSerie()
        resultado_label.config(
            text="Serie:\n" + ", ".join(map(str, resultado)),
            fg="#2c3e50"
        )
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")


# Crear ventana
ventana = tk.Tk()
ventana.title("Serie de Fibonacci")
ventana.geometry("500x300")
ventana.configure(bg="#f4f6f7")

# Widgets con estilo
titulo = tk.Label(
    ventana,
    text="Generador de Serie de Fibonacci",
    font=("Arial", 16, "bold"),
    bg="#f4f6f7",
    fg="#34495e"
)
titulo.pack(pady=15)

entry_label = tk.Label(
    ventana,
    text="Ingrese la cantidad de términos:",
    font=("Arial", 12),
    bg="#f4f6f7",
    fg="#2c3e50"
)
entry_label.pack()

entry = tk.Entry(
    ventana,
    justify="center",
    font=("Arial", 12),
    bd=2,
    relief="solid"
)
entry.pack(pady=8, ipadx=5, ipady=3)

btn = tk.Button(
    ventana,
    text="Generar Serie",
    command=calcular_fibonacci,
    font=("Arial", 12, "bold"),
    bg="#e67e22",  # naranja
    fg="white",
    activebackground="#d35400",
    activeforeground="white",
    relief="flat",
    padx=15,
    pady=5
)
btn.pack(pady=12)

resultado_label = tk.Label(
    ventana,
    text="",
    wraplength=450,
    justify="left",
    font=("Arial", 11),
    bg="#ecf0f1",
    fg="#0d0d0d",
    bd=0,
    relief="solid"
)
resultado_label.pack(pady=15, fill="x", padx=20)

ventana.mainloop()
