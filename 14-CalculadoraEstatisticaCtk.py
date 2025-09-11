import customtkinter as ctk

class CalculadoraEstadistica:
    def __init__(self, datos):
        self.datos = datos

    def media(self):    
        return sum(self.datos) / len(self.datos)
    
    def var(self):
        media = self.media()
        return sum((x - media)**2 for x in self.datos) / len(self.datos)
    
    def desvacion(self):
        return self.var() ** 0.5

def calcular():
    try:
        datos = [float(x) for x in entry_datos.get().split(",") if x.strip() != ""]
        if not datos:
            raise ValueError
        calculadora = CalculadoraEstadistica(datos)
        media = calculadora.media()
        varianza = calculadora.var()
        desviacion = calculadora.desvacion()
        resultado = (
            f"La Media es: {media:.2f}\n"
            f"La Varianza es: {varianza:.2f}\n"
            f"La Desviación estándar es: {desviacion:.2f}"
        )
        text_resultado.configure(state="normal")
        text_resultado.delete("1.0", "end")
        text_resultado.insert("end", resultado)
        text_resultado.configure(state="disabled")
    except Exception:
        text_resultado.configure(state="normal")
        text_resultado.delete("1.0", "end")
        text_resultado.insert("end", "Error: Ingrese una lista de números separados por coma.")
        text_resultado.configure(state="disabled")

# Estilo oscuro y minimalista
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Calculadora Estadística")
root.geometry("400x320")
root.resizable(False, False)
root.configure(fg_color="#181A1B")  # Fondo principal oscuro

frame = ctk.CTkFrame(root, fg_color="#232526", corner_radius=16)
frame.pack(padx=32, pady=32, fill="both", expand=True)

label = ctk.CTkLabel(
    frame,
    text="Ingrese los datos separados por coma:",
    font=ctk.CTkFont(size=16, weight="bold"),
    text_color="#E0E0E0"
)
label.pack(anchor="w", pady=(10, 2))

entry_datos = ctk.CTkEntry(
    frame,
    width=320,
    height=36,
    font=ctk.CTkFont(size=14),
    fg_color="#181A1B",
    border_color="#3A3B3C",
    border_width=2,
    text_color="#F5F5F5"
)
entry_datos.pack(pady=(0, 12))

btn_calcular = ctk.CTkButton(
    frame,
    text="Calcular",
    fg_color="#1A73E8",
    hover_color="#1761C7",
    text_color="#FFFFFF",
    font=ctk.CTkFont(size=15, weight="bold"),
    corner_radius=8,
    width=120,
    height=36
)
btn_calcular.configure(command=calcular)
btn_calcular.pack(pady=(0, 16))

text_resultado = ctk.CTkTextbox(
    frame,
    width=320,
    height=90,
    font=ctk.CTkFont(size=14),
    fg_color="#181A1B",
    border_color="#3A3B3C",
    border_width=2,
    text_color="#B0BEC5",
    state="disabled"
)
text_resultado.pack(pady=(0, 10))

root.mainloop()