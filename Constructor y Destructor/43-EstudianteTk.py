import customtkinter as ctk
import gc

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        return f"{self.nombre} estudia {self.carrera} y tiene {self.edad} años."

    def __del__(self):
        print(f"Estudiante eliminado: {self.nombre}")  # sigue apareciendo en consola


# --- Funciones de la interfaz ---
def registrar_estudiante():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    carrera = entry_carrera.get()

    if not nombre or not edad or not carrera:
        salida.insert("end", "⚠️ Por favor completa todos los campos.\n")
        return

    try:
        edad = int(edad)
    except ValueError:
        salida.insert("end", "⚠️ La edad debe ser un número.\n")
        return

    estudiante = Estudiante(nombre, edad, carrera)
    grupo.append(estudiante)
    salida.insert("end", f"Estudiante registrado: {nombre}, {edad} años, {carrera}\n")
    entry_nombre.delete(0, "end")
    entry_edad.delete(0, "end")
    entry_carrera.delete(0, "end")

def mostrar_informacion():
    if not grupo:
        salida.insert("end", "⚠️ No hay estudiantes registrados.\n")
        return
    salida.insert("end", "\n--- Información de estudiantes ---\n")
    for estudiante in grupo:
        salida.insert("end", estudiante.mostrar_informacion() + "\n")

def eliminar_estudiantes():
    global grupo
    if not grupo:
        salida.insert("end", "⚠️ No hay estudiantes para eliminar.\n")
        return
    grupo.clear()
    gc.collect()
    salida.insert("end", "\n⚠️ Estudiantes eliminados.\nFin de programa.\n")

def reiniciar_programa():
    global grupo
    grupo.clear()
    gc.collect()
    entry_nombre.delete(0, "end")
    entry_edad.delete(0, "end")
    entry_carrera.delete(0, "end")
    salida.delete("1.0", "end")
    salida.insert("end", "🔄 Programa reiniciado.\n")


# --- Configuración de ventana ---
ctk.set_appearance_mode("dark")   # "light" o "dark"
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Gestión de Estudiantes")
ventana.geometry("600x520")
ventana.resizable(False, False)

grupo = []

# --- Título ---
titulo = ctk.CTkLabel(ventana, text="Gestión de Estudiantes", font=("Segoe UI", 20, "bold"))
titulo.pack(pady=15)

# --- Entradas ---
frame_inputs = ctk.CTkFrame(ventana, corner_radius=12)
frame_inputs.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(frame_inputs, text="Nombre:", font=("Segoe UI", 13)).pack(pady=5)
entry_nombre = ctk.CTkEntry(frame_inputs, placeholder_text="Escribe el nombre...")
entry_nombre.pack(pady=5, padx=10, fill="x")

ctk.CTkLabel(frame_inputs, text="Edad:", font=("Segoe UI", 13)).pack(pady=5)
entry_edad = ctk.CTkEntry(frame_inputs, placeholder_text="Edad")
entry_edad.pack(pady=5, padx=10, fill="x")

ctk.CTkLabel(frame_inputs, text="Carrera:", font=("Segoe UI", 13)).pack(pady=5)
entry_carrera = ctk.CTkEntry(frame_inputs, placeholder_text="Carrera universitaria")
entry_carrera.pack(pady=5, padx=10, fill="x")

# --- Botones ---
frame_botones = ctk.CTkFrame(ventana, fg_color="transparent")
frame_botones.pack(pady=15)

btn_registrar = ctk.CTkButton(frame_botones, text="Registrar", command=registrar_estudiante)
btn_registrar.grid(row=0, column=0, padx=10)

btn_mostrar = ctk.CTkButton(frame_botones, text="Mostrar información", command=mostrar_informacion)
btn_mostrar.grid(row=0, column=1, padx=10)

btn_eliminar = ctk.CTkButton(frame_botones, text="Eliminar", command=eliminar_estudiantes)
btn_eliminar.grid(row=0, column=2, padx=10)

btn_reiniciar = ctk.CTkButton(frame_botones, text="Reiniciar", command=reiniciar_programa, fg_color="#d9534f", hover_color="#c9302c")
btn_reiniciar.grid(row=0, column=3, padx=10)

# --- Área de salida ---
salida = ctk.CTkTextbox(ventana, width=560, height=200, wrap="word", font=("Consolas", 12))
salida.pack(pady=15, padx=20)

ventana.mainloop()
