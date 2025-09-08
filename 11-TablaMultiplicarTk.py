import tkinter as tk
from tkinter import messagebox

class TablaMultiplicar:
    def __init__(self, numero):
        self.numero = numero
        self.resultados = []

    def generarTabla(self):
        for i in range(1, 11):
            self.resultados.append(f"{self.numero} x {i} = {self.numero * i}")
        return self.resultados


def calcular_tabla():
    try:
        numero = int(entry.get())
        miTabla = TablaMultiplicar(numero)
        resultado = miTabla.generarTabla()
        
        # Mostrar la tabla en el label
        resultado_label.config(
            text="\n".join(resultado),
            fg="#2c3e50"
        )
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")


# Crear ventana
ventana = tk.Tk()
ventana.title("Tabla de Multiplicar")
ventana.geometry("450x450")
ventana.configure(bg="#f4f6f7")

# Widgets con estilo
titulo = tk.Label(
    ventana,
    text="Generador de Tablas de Multiplicar",
    font=("Arial", 16, "bold"),
    bg="#f4f6f7",
    fg="#0d0d0d"
)
titulo.pack(pady=15)

entry_label = tk.Label(
    ventana,
    text="Ingrese un número:",
    font=("Arial", 12),
    bg="#f4f6f7",
    fg="#040f1a"
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
    text="Generar",
    command=calcular_tabla,
    font=("Arial", 12, "bold"),
    bg="#e67e22",   # naranja
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
    justify="left",
    font=("Consolas", 12),  # Monoespaciada para que se vea alineado
    bg="#ecf0f1",
    fg="#131415",
    bd=0,
    relief="solid"
)
resultado_label.pack(pady=15, fill="x", padx=20)

ventana.mainloop()
