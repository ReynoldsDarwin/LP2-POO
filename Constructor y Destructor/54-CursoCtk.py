import customtkinter as ctk
import gc

class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor

    def mostrar_informacion(self):
        return f"Curso Registrado: {self.nombre} | Código: {self.codigo} | Docente: {self.profesor}"

    def __del__(self):
        print(f"Curso eliminado: {self.nombre}")  # solo consola


# --- Funciones ---
def registrar_curso():
    nombre = entry_nombre.get()
    codigo = entry_codigo.get()
    profesor = entry_profesor.get()

    if not nombre or not codigo or not profesor:
        salida.insert("end", "⚠️ Por favor completa todos los campos.\n")
        return

    try:
        codigo = int(codigo)
    except ValueError:
        salida.insert("end", "⚠️ El código debe ser un número.\n")
        return

    curso = Curso(nombre, codigo, profesor)
    cursos.append(curso)
    salida.insert("end", f"Curso registrado: {nombre}, código {codigo}, docente {profesor}\n")

    entry_nombre.delete(0, "end")
    entry_codigo.delete(0, "end")
    entry_profesor.delete(0, "end")

def mostrar_informacion():
    if not cursos:
        salida.insert("end", "⚠️ No hay cursos registrados.\n")
        return
    salida.insert("end", "\n--- Información de cursos ---\n")
    for curso in cursos:
        salida.insert("end", curso.mostrar_informacion() + "\n")

def eliminar_cursos():
    global cursos
    if not cursos:
        salida.insert("end", "⚠️ No hay cursos para eliminar.\n")
        return
    cursos.clear()
    gc.collect()
    salida.insert("end", "\n⚠️ Cursos eliminados.\nFin del programa.\n")

def reiniciar_programa():
    global cursos
    cursos.clear()
    gc.collect()
    entry_nombre.delete(0, "end")
    entry_codigo.delete(0, "end")
    entry_profesor.delete(0, "end")
    salida.delete("1.0", "end")
    salida.insert("end", "🔄 Programa reiniciado.\n")


# --- Configuración ventana ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Gestión de Cursos")
ventana.geometry("600x520")
ventana.resizable(False, False)

cursos = []

# --- Título ---
titulo = ctk.CTkLabel(ventana, text="Gestión de Cursos", font=("Segoe UI", 20, "bold"))
titulo.pack(pady=15)

# --- Entradas ---
frame_inputs = ctk.CTkFrame(ventana, corner_radius=12)
frame_inputs.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(frame_inputs, text="Nombre del curso:", font=("Segoe UI", 13)).pack(pady=5)
entry_nombre = ctk.CTkEntry(frame_inputs, placeholder_text="Ejemplo: Matemáticas")
entry_nombre.pack(pady=5, padx=10, fill="x")

ctk.CTkLabel(frame_inputs, text="Código del curso:", font=("Segoe UI", 13)).pack(pady=5)
entry_codigo = ctk.CTkEntry(frame_inputs, placeholder_text="Ejemplo: 101")
entry_codigo.pack(pady=5, padx=10, fill="x")

ctk.CTkLabel(frame_inputs, text="Docente del curso:", font=("Segoe UI", 13)).pack(pady=5)
entry_profesor = ctk.CTkEntry(frame_inputs, placeholder_text="Ejemplo: Juan Pérez")
entry_profesor.pack(pady=5, padx=10, fill="x")

# --- Botones ---
frame_botones = ctk.CTkFrame(ventana, fg_color="transparent")
frame_botones.pack(pady=15)

btn_registrar = ctk.CTkButton(frame_botones, text="Registrar", command=registrar_curso)
btn_registrar.grid(row=0, column=0, padx=10)

btn_mostrar = ctk.CTkButton(frame_botones, text="Mostrar información", command=mostrar_informacion)
btn_mostrar.grid(row=0, column=1, padx=10)

btn_eliminar = ctk.CTkButton(frame_botones, text="Eliminar", command=eliminar_cursos)
btn_eliminar.grid(row=0, column=2, padx=10)

btn_reiniciar = ctk.CTkButton(frame_botones, text="Reiniciar", command=reiniciar_programa,
                              fg_color="#d9534f", hover_color="#c9302c")
btn_reiniciar.grid(row=0, column=3, padx=10)

# --- Área de salida ---
salida = ctk.CTkTextbox(ventana, width=560, height=200, wrap="word", font=("Consolas", 12))
salida.pack(pady=15, padx=20)

ventana.mainloop()
