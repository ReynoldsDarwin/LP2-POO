import customtkinter as ctk
from tkinter import messagebox


# ================== CLASES ORIGINALES ==================
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola soy {self.nombre} y tengo {self.edad} años."


class Trabajador:
    def __init__(self, profesion, salario):
        self.profesion = profesion
        self.salario = salario

    def trabajar(self):
        return f"Estoy trabajando como {self.profesion} y gano ${self.salario} al mes."


class Estudiante:
    def __init__(self, carrera, universidad):
        self.carrera = carrera
        self.universidad = universidad

    def estudiar(self):
        return f"Estudio {self.carrera} en la {self.universidad}."


class PersonaMultirol(Persona, Trabajador, Estudiante):
    def __init__(self, nombre, edad, profesion, salario, carrera, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, profesion, salario)
        Estudiante.__init__(self, carrera, universidad)

    def mostrar_informacion(self):
        info = "\n===== INFORMACIÓN DE LA PERSONA =====\n"
        info += self.presentarse() + "\n"
        info += self.trabajar() + "\n"
        info += self.estudiar() + "\n"
        return info


# ================== INTERFAZ GRÁFICA ==================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("👩‍💼 Registro de Personas Multirol")
ventana.geometry("850x600")

# Lista para almacenar todas las personas registradas
personas_registradas = []


def registrar_persona():
    """Crea un nuevo registro y lo muestra en terminal."""
    try:
        nombre = entry_nombre.get()
        edad = int(entry_edad.get())
        profesion = entry_profesion.get()
        salario = float(entry_salario.get())
        carrera = entry_carrera.get()
        universidad = entry_universidad.get()

        if not all([nombre, profesion, carrera, universidad]):
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return

        persona = PersonaMultirol(nombre, edad, profesion, salario, carrera, universidad)
        personas_registradas.append(persona)

        # Mostrar en terminal (acumulativo)
        print(persona.mostrar_informacion())
        print(f"Total de registros acumulados: {len(personas_registradas)}")
        print("=" * 60)

        # Mostrar en interfaz también
        text_salida.configure(state="normal")
        text_salida.insert("end", persona.mostrar_informacion() + "\n")
        text_salida.configure(state="disabled")

    except ValueError:
        messagebox.showerror("Error", "Edad y salario deben ser numéricos.")


def reiniciar():
    """Limpia los campos del formulario, pero mantiene los registros acumulados."""
    for entry in [entry_nombre, entry_edad, entry_profesion, entry_salario, entry_carrera, entry_universidad]:
        entry.delete(0, "end")


# ================== COMPONENTES DE LA INTERFAZ ==================
titulo = ctk.CTkLabel(ventana, text="👩‍💼 REGISTRO DE PERSONAS MULTIROL", font=("Segoe UI", 24, "bold"))
titulo.pack(pady=15)

frame_inputs = ctk.CTkFrame(ventana)
frame_inputs.pack(pady=10, padx=20, fill="x")

# Campos
ctk.CTkLabel(frame_inputs, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nombre = ctk.CTkEntry(frame_inputs, placeholder_text="Ej: Juanita")
entry_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="w")

ctk.CTkLabel(frame_inputs, text="Edad:").grid(row=0, column=2, padx=10, pady=5, sticky="e")
entry_edad = ctk.CTkEntry(frame_inputs, placeholder_text="Ej: 25")
entry_edad.grid(row=0, column=3, padx=10, pady=5, sticky="w")

ctk.CTkLabel(frame_inputs, text="Profesión:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_profesion = ctk.CTkEntry(frame_inputs, placeholder_text="Ej: Desarrollador de Software")
entry_profesion.grid(row=1, column=1, padx=10, pady=5, sticky="w")

ctk.CTkLabel(frame_inputs, text="Salario ($):").grid(row=1, column=2, padx=10, pady=5, sticky="e")
entry_salario = ctk.CTkEntry(frame_inputs, placeholder_text="Ej: 2500")
entry_salario.grid(row=1, column=3, padx=10, pady=5, sticky="w")

ctk.CTkLabel(frame_inputs, text="Carrera:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_carrera = ctk.CTkEntry(frame_inputs, placeholder_text="Ej: Ingeniería Estadística e Informática")
entry_carrera.grid(row=2, column=1, padx=10, pady=5, sticky="w")

ctk.CTkLabel(frame_inputs, text="Universidad:").grid(row=2, column=2, padx=10, pady=5, sticky="e")
entry_universidad = ctk.CTkEntry(frame_inputs, placeholder_text="Ej: Universidad Nacional del Altiplano")
entry_universidad.grid(row=2, column=3, padx=10, pady=5, sticky="w")

# --- Botones ---
frame_botones = ctk.CTkFrame(ventana)
frame_botones.pack(pady=15)

ctk.CTkButton(frame_botones, text="Registrar Persona", fg_color="#27AE60", width=180, command=registrar_persona).grid(row=0, column=0, padx=15)
ctk.CTkButton(frame_botones, text="Reiniciar Campos", fg_color="#E74C3C", hover_color="#C0392B", width=150, command=reiniciar).grid(row=0, column=1, padx=15)

# --- Área de salida ---
text_salida = ctk.CTkTextbox(ventana, width=800, height=250, font=("Consolas", 13))
text_salida.pack(pady=10)
text_salida.configure(state="disabled")

ctk.CTkLabel(ventana, text="Desarrollado con ❤️ en CustomTkinter", font=("Segoe UI", 11, "italic")).pack(pady=10)

ventana.mainloop()
