import customtkinter as ctk
import gc

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio  = anio

    def mostrar_informacion(self):
        return f"Libro registrado: {self.titulo} de {self.autor} ({self.anio})"

    def __del__(self):
        print(f"Libro eliminado: {self.titulo}")  # se muestra en consola


# --- Funciones ---
def registrar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    anio = entry_anio.get()

    if not titulo or not autor or not anio:
        salida.insert("end", "⚠️ Por favor completa todos los campos.\n")
        return

    try:
        anio = int(anio)
    except ValueError:
        salida.insert("end", "⚠️ El año debe ser un número.\n")
        return

    libro = Libro(titulo, autor, anio)
    biblioteca.append(libro)
    salida.insert("end", libro.mostrar_informacion() + "\n")

    entry_titulo.delete(0, "end")
    entry_autor.delete(0, "end")
    entry_anio.delete(0, "end")

def mostrar_informacion():
    if not biblioteca:
        salida.insert("end", "⚠️ No hay libros registrados.\n")
        return
    salida.insert("end", "\n--- Información de libros ---\n")
    for libro in biblioteca:
        salida.insert("end", libro.mostrar_informacion() + "\n")

def eliminar_libros():
    global biblioteca
    if not biblioteca:
        salida.insert("end", "⚠️ No hay libros para eliminar.\n")
        return
    biblioteca.clear()
    gc.collect()
    salida.insert("end", "\n⚠️ Libros eliminados.\nFin del programa.\n")

def reiniciar_programa():
    global biblioteca
    biblioteca.clear()
    gc.collect()
    entry_titulo.delete(0, "end")
    entry_autor.delete(0, "end")
    entry_anio.delete(0, "end")
    salida.delete("1.0", "end")
    salida.insert("end", "🔄 Programa reiniciado.\n")


# --- Configuración ventana ---
ctk.set_appearance_mode("dark")   # "light" o "dark"
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Gestión de Biblioteca")
ventana.geometry("600x520")
ventana.resizable(False, False)

biblioteca = []

# --- Título ---
titulo = ctk.CTkLabel(ventana, text="Gestión de Biblioteca", font=("Segoe UI", 20, "bold"))
titulo.pack(pady=15)

# --- Entradas ---
frame_inputs = ctk.CTkFrame(ventana, corner_radius=12)
frame_inputs.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(frame_inputs, text="Título:", font=("Segoe UI", 13)).pack(pady=5)
entry_titulo = ctk.CTkEntry(frame_inputs, placeholder_text="Escribe el título del libro...")
entry_titulo.pack(pady=5, padx=10, fill="x")

ctk.CTkLabel(frame_inputs, text="Autor:", font=("Segoe UI", 13)).pack(pady=5)
entry_autor = ctk.CTkEntry(frame_inputs, placeholder_text="Escribe el autor...")
entry_autor.pack(pady=5, padx=10, fill="x")

ctk.CTkLabel(frame_inputs, text="Año de publicación:", font=("Segoe UI", 13)).pack(pady=5)
entry_anio = ctk.CTkEntry(frame_inputs, placeholder_text="Ejemplo: 1995")
entry_anio.pack(pady=5, padx=10, fill="x")

# --- Botones ---
frame_botones = ctk.CTkFrame(ventana, fg_color="transparent")
frame_botones.pack(pady=15)

btn_registrar = ctk.CTkButton(frame_botones, text="Registrar", command=registrar_libro)
btn_registrar.grid(row=0, column=0, padx=10)

btn_mostrar = ctk.CTkButton(frame_botones, text="Mostrar información", command=mostrar_informacion)
btn_mostrar.grid(row=0, column=1, padx=10)

btn_eliminar = ctk.CTkButton(frame_botones, text="Eliminar", command=eliminar_libros)
btn_eliminar.grid(row=0, column=2, padx=10)

btn_reiniciar = ctk.CTkButton(frame_botones, text="Reiniciar", command=reiniciar_programa, fg_color="#d9534f", hover_color="#c9302c")
btn_reiniciar.grid(row=0, column=3, padx=10)

# --- Área de salida ---
salida = ctk.CTkTextbox(ventana, width=560, height=200, wrap="word", font=("Consolas", 12))
salida.pack(pady=15, padx=20)

ventana.mainloop()
