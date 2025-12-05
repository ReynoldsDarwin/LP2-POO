from typing import TypeVar, Generic
import customtkinter as ctk
from tkinter import messagebox

T = TypeVar('T', int, float)

class Calculadora(Generic[T]):
    def __init__(self, a: T, b: T):
        self.a = a
        self.b = b

    def sumar(self) -> T:
        return self.a + self.b

    def restar(self) -> T:
        return self.a - self.b

    def multiplicar(self) -> T:
        return self.a * self.b

    def dividir(self) -> T:
        if self.b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return self.a / self.b


# -------------- INTERFAZ GRÁFICA TIPO CALCULADORA -------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Calculadora Pro")
app.geometry("340x500")
app.resizable(False, False)

# Pantalla
pantalla = ctk.CTkEntry(app, width=300, height=70, justify="right",
                        font=("Consolas", 28), corner_radius=12)
pantalla.pack(pady=20)

# Variables internas
operador = ""
valor_a = None

def seleccionar_numero(num):
    pantalla.insert("end", num)

def limpiar():
    global operador, valor_a
    operador = ""
    valor_a = None
    pantalla.delete(0, "end")

def seleccionar_operacion(op):
    global operador, valor_a
    try:
        valor_a = float(pantalla.get())
        operador = op
        pantalla.delete(0, "end")
    except:
        messagebox.showerror("Error", "Primero ingresa un número válido.")

def calcular():
    global operador, valor_a
    try:
        valor_b = float(pantalla.get())
        calc = Calculadora(valor_a, valor_b)

        if operador == "+":
            resultado = calc.sumar()
        elif operador == "-":
            resultado = calc.restar()
        elif operador == "*":
            resultado = calc.multiplicar()
        elif operador == "/":
            resultado = calc.dividir()
        else:
            return

        pantalla.delete(0, "end")
        pantalla.insert(0, str(resultado))
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- BOTONES ---------------- #

frame = ctk.CTkFrame(app)
frame.pack()

botones = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3)
]

for (texto, fila, col) in botones:
    if texto.isdigit() or texto == ".":
        cmd = lambda t=texto: seleccionar_numero(t)
    elif texto == "=":
        cmd = calcular
    else:
        cmd = lambda t=texto: seleccionar_operacion(t)

    btn = ctk.CTkButton(
        frame,
        text=texto,
        width=65,
        height=65,
        font=("Arial", 24),
        corner_radius=12,
        command=cmd
    )
    btn.grid(row=fila, column=col, padx=5, pady=5)

# Botón limpiar (C)
btn_clear = ctk.CTkButton(app, text="Limpiar", width=300, height=45,
                          font=("Arial", 18), corner_radius=12, fg_color="#cc3333",
                          command=limpiar)
btn_clear.pack(pady=10)

app.mainloop()
