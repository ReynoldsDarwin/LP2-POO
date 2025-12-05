from typing import TypeVar, Generic
import customtkinter as ctk
import math
from tkinter import Canvas

T = TypeVar("T")

# -------------------- CLASES -------------------- #

class Figura(Generic[T]):
    def __init__(self, valor: T):
        self.valor = valor

    def area(self) -> float:
        pass

    def perimetro(self) -> float:
        pass


class Rectangulo(Figura[float]):
    def __init__(self, base: float, altura: float):
        super().__init__(None)
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)


class Circulo(Figura[float]):
    def __init__(self, radio: float):
        super().__init__(None)
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio**2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio


# -------------------- INTERFAZ -------------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Figuras Geométricas Pro")
app.geometry("650x550")
app.resizable(False, False)

titulo = ctk.CTkLabel(app, text="Visualizador de Figuras Geométricas",
                      font=("Arial", 24, "bold"))
titulo.pack(pady=15)

# FRAME PRINCIPAL
frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(pady=10, padx=10, fill="both", expand=True)

# CANVAS PARA DIBUJO
canvas = Canvas(frame, width=350, height=350, bg="#0A0A0A", highlightthickness=0)
canvas.grid(row=0, column=1, rowspan=10, padx=20, pady=20)

# CAMPOS DE ENTRADA
label_tipo = ctk.CTkLabel(frame, text="Selecciona una figura:", font=("Arial", 16))
label_tipo.grid(row=0, column=0, pady=10)

opcion = ctk.CTkComboBox(frame, values=["Rectángulo", "Círculo"], width=180)
opcion.grid(row=1, column=0, pady=10)
opcion.set("Rectángulo")

entry1 = ctk.CTkEntry(frame, placeholder_text="Base (Rectángulo) / Radio (Círculo)", width=180)
entry1.grid(row=2, column=0, pady=10)

entry2 = ctk.CTkEntry(frame, placeholder_text="Altura (Rectángulo)", width=180)
entry2.grid(row=3, column=0, pady=10)

# ETIQUETAS DE RESULTADO
resultado_area = ctk.CTkLabel(frame, text="Área: --", font=("Arial", 16))
resultado_area.grid(row=5, column=0, pady=10)

resultado_perimetro = ctk.CTkLabel(frame, text="Perímetro: --", font=("Arial", 16))
resultado_perimetro.grid(row=6, column=0, pady=10)


# -------------------- LÓGICA -------------------- #

def dibujar_rectangulo(base, altura):
    canvas.delete("all")

    # Escalado automático
    scale = 250 / max(base, altura)
    b = base * scale
    h = altura * scale

    x0 = (350 - b) / 2
    y0 = (350 - h) / 2
    x1 = x0 + b
    y1 = y0 + h

    canvas.create_rectangle(x0, y0, x1, y1, outline="#00BFFF", width=3)
    canvas.create_text(175, 20, text=f"{base} x {altura}", fill="white", font=("Arial", 14))


def dibujar_circulo(radio):
    canvas.delete("all")

    scale = 120 / radio
    r = radio * scale

    canvas.create_oval(175 - r, 175 - r, 175 + r, 175 + r,
                       outline="#32CD32", width=3)
    canvas.create_text(175, 20, text=f"Radio = {radio}", fill="white", font=("Arial", 14))


def calcular():
    try:
        tipo = opcion.get()

        valor1 = float(entry1.get())
        valor2 = None

        if tipo == "Rectángulo":
            valor2 = float(entry2.get())
            fig = Rectangulo(valor1, valor2)
            dibujar_rectangulo(valor1, valor2)
        else:
            fig = Circulo(valor1)
            dibujar_circulo(valor1)

        resultado_area.configure(text=f"Área: {fig.area():.2f}")
        resultado_perimetro.configure(text=f"Perímetro: {fig.perimetro():.2f}")

    except ValueError:
        resultado_area.configure(text="Error: Ingresa números válidos")
        resultado_perimetro.configure(text="")



# BOTÓN CALCULAR
boton = ctk.CTkButton(frame, text="Calcular", font=("Arial", 18), width=180, command=calcular)
boton.grid(row=4, column=0, pady=15)


app.mainloop()
