import customtkinter as ctk
from tkinter import StringVar
from datetime import datetime

class Persona:
    def __init__(self, nombre, dia, mes):
        self.nombre = nombre
        self.dia = dia
        self.mes = mes

    def signo_zodiacal(self):
        signos = [
            ("Capricornio", (12, 22), (1, 19)),
            ("Acuario", (1, 20), (2, 18)),
            ("Piscis", (2, 19), (3, 20)),
            ("Aries", (3, 21), (4, 19)),
            ("Tauro", (4, 20), (5, 20)),
            ("Géminis", (5, 21), (6, 20)),
            ("Cáncer", (6, 21), (7, 22)),
            ("Leo", (7, 23), (8, 22)),
            ("Virgo", (8, 23), (9, 22)),
            ("Libra", (9, 23), (10, 22)),
            ("Escorpio", (10, 23), (11, 21)),
            ("Sagitario", (11, 22), (12, 21)),
        ]
        for signo, inicio, fin in signos:
            if (self.mes == inicio[0] and self.dia >= inicio[1]) or (self.mes == fin[0] and self.dia <= fin[1]):
                return signo
        return "Desconocido"


def calcular_signo():
    try:
        nombre = entry_nombre.get()
        dia = int(combo_dia.get())
        mes_nombre = combo_mes.get()

        meses_dict = {
            "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
            "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
            "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
        }
        mes = meses_dict[mes_nombre]

        datetime(year=2000, month=mes, day=dia)  # validación de fecha

        persona = Persona(nombre, dia, mes)
        signo = persona.signo_zodiacal()

        resultado.set(f"Hola {persona.nombre}, naciste el {dia} de {mes_nombre} y tu signo zodiacal es: {signo}.")
    except Exception:
        resultado.set("⚠️ Ingresa una fecha válida")

def reiniciar():
    entry_nombre.delete(0, "end")
    combo_dia.set("")
    combo_mes.set("")
    resultado.set("")

# Configuración de la ventana principal 
ctk.set_appearance_mode("dark")   
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Calculadora de Signo Zodiacal")
ventana.geometry("520x480")  
ventana.resizable(False, False)

resultado = StringVar()

# --- Widgets ---
titulo = ctk.CTkLabel(ventana, text="Conoce tu Signo Zodiacal", font=("Segoe UI", 20, "bold"))
titulo.pack(pady=15)

frame = ctk.CTkFrame(ventana, corner_radius=12)
frame.pack(pady=15, padx=25, fill="both", expand=True)

# Nombre
label_nombre = ctk.CTkLabel(frame, text="Nombre:", font=("Segoe UI", 13))
label_nombre.pack(pady=(10, 3))
entry_nombre = ctk.CTkEntry(frame, placeholder_text="Escribe tu nombre...")
entry_nombre.pack(pady=5)

# Día
label_dia = ctk.CTkLabel(frame, text="Día de nacimiento:", font=("Segoe UI", 13))
label_dia.pack(pady=(10, 3))
combo_dia = ctk.CTkComboBox(frame, values=[str(i) for i in range(1, 32)], width=120)
combo_dia.pack(pady=5)

# Mes
label_mes = ctk.CTkLabel(frame, text="Mes de nacimiento:", font=("Segoe UI", 13))
label_mes.pack(pady=(10, 3))
meses = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
]
combo_mes = ctk.CTkComboBox(frame, values=meses, width=160)
combo_mes.pack(pady=5)

# Botones
frame_botones = ctk.CTkFrame(frame, fg_color="transparent")
frame_botones.pack(pady=20)

btn_calcular = ctk.CTkButton(frame_botones, text="Calcular signo", command=calcular_signo)
btn_calcular.grid(row=0, column=0, padx=10)

btn_reiniciar = ctk.CTkButton(frame_botones, text="⭮", width=40, command=reiniciar)
btn_reiniciar.grid(row=0, column=1, padx=10)

# Resultado
label_resultado = ctk.CTkLabel(frame, textvariable=resultado, font=("Segoe UI", 15), wraplength=450, justify="center")
label_resultado.pack(pady=20)

ventana.mainloop()
