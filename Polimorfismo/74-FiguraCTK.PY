import customtkinter as ctk
import math
from tkinter import messagebox

# ================== CLASES ORIGINALES ==================
class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * (self.radio ** 2)

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2


# ================== INTERFAZ GRÁFICA ==================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("📐 Calculadora de Áreas - Visual con Figuras")
ventana.geometry("750x700")

# Variables
figura_seleccionada = ctk.StringVar(value="Cuadrado")

# ================== FUNCIONES ==================
def mostrar_campos(*args):
    """Muestra los campos según la figura seleccionada."""
    for widget in frame_campos.winfo_children():
        widget.destroy()

    fig = figura_seleccionada.get()

    if fig == "Cuadrado":
        ctk.CTkLabel(frame_campos, text="Lado:").grid(row=0, column=0, padx=10, pady=10)
        entry_lado = ctk.CTkEntry(frame_campos, placeholder_text="Ej: 4")
        entry_lado.grid(row=0, column=1, padx=10, pady=10)
        frame_campos.entrys = [entry_lado]

    elif fig == "Círculo":
        ctk.CTkLabel(frame_campos, text="Radio:").grid(row=0, column=0, padx=10, pady=10)
        entry_radio = ctk.CTkEntry(frame_campos, placeholder_text="Ej: 3")
        entry_radio.grid(row=0, column=1, padx=10, pady=10)
        frame_campos.entrys = [entry_radio]

    elif fig == "Triángulo":
        ctk.CTkLabel(frame_campos, text="Base:").grid(row=0, column=0, padx=10, pady=10)
        entry_base = ctk.CTkEntry(frame_campos, placeholder_text="Ej: 5")
        entry_base.grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkLabel(frame_campos, text="Altura:").grid(row=1, column=0, padx=10, pady=10)
        entry_altura = ctk.CTkEntry(frame_campos, placeholder_text="Ej: 2")
        entry_altura.grid(row=1, column=1, padx=10, pady=10)
        frame_campos.entrys = [entry_base, entry_altura]


def calcular_area():
    """Calcula el área según la figura seleccionada y la dibuja."""
    try:
        fig = figura_seleccionada.get()
        canvas.delete("all")  # Limpiar dibujo previo

        if fig == "Cuadrado":
            lado = float(frame_campos.entrys[0].get())
            figura = Cuadrado(lado)
            resultado = figura.area()
            label_resultado.configure(text=f"Área del cuadrado: {resultado:.2f}")
            dibujar_cuadrado(lado, resultado)

        elif fig == "Círculo":
            radio = float(frame_campos.entrys[0].get())
            figura = Circulo(radio)
            resultado = figura.area()
            label_resultado.configure(text=f"Área del círculo: {resultado:.2f}")
            dibujar_circulo(radio, resultado)

        elif fig == "Triángulo":
            base = float(frame_campos.entrys[0].get())
            altura = float(frame_campos.entrys[1].get())
            figura = Triangulo(base, altura)
            resultado = figura.area()
            label_resultado.configure(text=f"Área del triángulo: {resultado:.2f}")
            dibujar_triangulo(base, altura, resultado)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")


def reiniciar():
    """Reinicia los campos, el resultado y el dibujo."""
    for widget in frame_campos.winfo_children():
        widget.destroy()
    label_resultado.configure(text="Área: ---")
    canvas.delete("all")
    mostrar_campos()


# ================== FUNCIONES DE DIBUJO ==================
def dibujar_cuadrado(lado, area):
    escala = 20
    tamaño = lado * escala
    x0, y0 = 150, 120
    x1, y1 = x0 + tamaño, y0 + tamaño
    canvas.create_rectangle(x0, y0, x1, y1, fill="#3498DB", outline="white", width=2)
    canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=f"{area:.2f}", fill="white", font=("Consolas", 16, "bold"))


def dibujar_circulo(radio, area):
    escala = 20
    r = radio * escala
    x0, y0 = 300 - r, 150 - r
    x1, y1 = 300 + r, 150 + r
    canvas.create_oval(x0, y0, x1, y1, fill="#E67E22", outline="white", width=2)
    canvas.create_text(300, 150, text=f"{area:.2f}", fill="white", font=("Consolas", 16, "bold"))


def dibujar_triangulo(base, altura, area):
    escala = 30
    b = base * escala
    h = altura * escala
    x0, y0 = 200, 250
    puntos = [x0, y0, x0 + b, y0, x0 + b / 2, y0 - h]
    canvas.create_polygon(puntos, fill="#9B59B6", outline="white", width=2)
    canvas.create_text(x0 + b / 2, y0 - h / 2, text=f"{area:.2f}", fill="white", font=("Consolas", 16, "bold"))


# ================== COMPONENTES DE INTERFAZ ==================
titulo = ctk.CTkLabel(ventana, text="📐 CALCULADORA DE ÁREAS", font=("Segoe UI", 22, "bold"))
titulo.pack(pady=15)

frame_opciones = ctk.CTkFrame(ventana)
frame_opciones.pack(pady=10)

ctk.CTkLabel(frame_opciones, text="Selecciona una figura:").grid(row=0, column=0, padx=10, pady=10)
menu_figuras = ctk.CTkOptionMenu(frame_opciones, variable=figura_seleccionada, values=["Cuadrado", "Círculo", "Triángulo"], command=mostrar_campos)
menu_figuras.grid(row=0, column=1, padx=10, pady=10)

frame_campos = ctk.CTkFrame(ventana)
frame_campos.pack(pady=10)
frame_campos.entrys = []

frame_botones = ctk.CTkFrame(ventana)
frame_botones.pack(pady=10)

ctk.CTkButton(frame_botones, text="Calcular Área", fg_color="#27AE60", command=calcular_area).grid(row=0, column=0, padx=10)
ctk.CTkButton(frame_botones, text="Reiniciar", fg_color="#E74C3C", hover_color="#C0392B", command=reiniciar).grid(row=0, column=1, padx=10)

label_resultado = ctk.CTkLabel(ventana, text="Área: ---", font=("Consolas", 18, "bold"))
label_resultado.pack(pady=10)

# Canvas donde se dibuja la figura
canvas_frame = ctk.CTkFrame(ventana)
canvas_frame.pack(pady=10)

canvas = ctk.CTkCanvas(canvas_frame, width=600, height=300, bg="#1A1A1A", highlightthickness=0)
canvas.pack()

ctk.CTkLabel(ventana, text="Desarrollado con CustomTkinter", font=("Segoe UI", 11, "italic")).pack(pady=10)

# Mostrar campos iniciales
mostrar_campos()

ventana.mainloop()
