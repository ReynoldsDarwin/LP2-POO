import tkinter as tk
from tkinter import messagebox

# ---------- CLASES ORIGINALES ----------
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f'✅ El libro "{self.titulo}" ha sido prestado.'
        else:
            return f'❌ El libro "{self.titulo}" no está disponible actualmente.'

    def devolver(self):
        self.disponible = True
        return f'📘 El libro "{self.titulo}" ha sido devuelto.'


class Prestamo:
    def __init__(self, libro, fecha_prestamo):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.devuelto = False

    def marcar_devolucion(self):
        self.devuelto = True
        return self.libro.devolver()


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos = []

    def realizar_prestamo(self, libro, fecha):
        if libro.disponible:
            msg = libro.prestar()
            prestamo = Prestamo(libro, fecha)
            self.prestamos.append(prestamo)
            return msg
        else:
            return f'❌ No se puede realizar el préstamo: "{libro.titulo}" no está disponible.'

    def mostrar_prestamo(self):
        texto = f'\n📄 Préstamos de {self.nombre}:\n'
        for p in self.prestamos:
            estado = 'Devuelto' if p.devuelto else 'Pendiente'
            texto += f' - {p.libro.titulo} ({estado}) - Fecha: {p.fecha_prestamo}\n'
        return texto


# ---------- FUNCIONES DE INTERFAZ ----------
def registrar_libros():
    try:
        cantidad = int(entry_cantidad.get())
    except ValueError:
        messagebox.showwarning("Error", "Por favor, ingresa un número válido.")
        return

    if cantidad <= 0:
        messagebox.showwarning("Error", "La cantidad debe ser mayor a 0.")
        return

    # Limpia campos previos si existen
    for widget in frame_libros.winfo_children():
        widget.destroy()
    libros_entries.clear()

    # Genera campos para cada libro
    for i in range(cantidad):
        tk.Label(frame_libros, text=f"Libro {i+1} - Título:").grid(row=i, column=0, padx=5, pady=2)
        e1 = tk.Entry(frame_libros)
        e1.grid(row=i, column=1, padx=5)

        tk.Label(frame_libros, text="Autor:").grid(row=i, column=2, padx=5)
        e2 = tk.Entry(frame_libros)
        e2.grid(row=i, column=3, padx=5)

        tk.Label(frame_libros, text="ISBN:").grid(row=i, column=4, padx=5)
        e3 = tk.Entry(frame_libros)
        e3.grid(row=i, column=5, padx=5)

        libros_entries.append((e1, e2, e3))

def registrar_usuario():
    global usuario1
    nombre = entry_nombre.get()
    id_usu = entry_id.get()
    if not nombre or not id_usu:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos del usuario.")
        return

    # Crear libros
    libros.clear()
    for (e1, e2, e3) in libros_entries:
        t, a, i = e1.get(), e2.get(), e3.get()
        if not t or not a or not i:
            messagebox.showwarning("Campos vacíos", "Completa todos los datos de los libros.")
            return
        libros.append(Libro(t, a, i))

    usuario1 = Usuario(nombre, id_usu)
    area_salida.insert("end", f"✅ Usuario {nombre} registrado con {len(libros)} libros.\n")

    # Crear campos de préstamo
    crear_campos_prestamo()

def crear_campos_prestamo():
    for widget in frame_prestamos.winfo_children():
        widget.destroy()
    prestamos_entries.clear()
    devolver_botones.clear()

    for i, libro in enumerate(libros):
        tk.Label(frame_prestamos, text=f"Fecha de préstamo de '{libro.titulo}':").grid(row=i, column=0, padx=5, pady=2)
        e = tk.Entry(frame_prestamos)
        e.grid(row=i, column=1, padx=5)
        prestamos_entries.append(e)

    tk.Button(frame_prestamos, text="Realizar Préstamos", bg="#4CAF50", fg="white", command=realizar_prestamos).grid(row=len(libros), column=0, pady=10)

def realizar_prestamos():
    for i, libro in enumerate(libros):
        fecha = prestamos_entries[i].get()
        if not fecha:
            messagebox.showwarning("Faltan datos", f"Ingrese la fecha del libro '{libro.titulo}'.")
            return
        msg = usuario1.realizar_prestamo(libro, fecha)
        area_salida.insert("end", msg + "\n")

    area_salida.insert("end", usuario1.mostrar_prestamo() + "\n")

    # Botones para devolver libros
    for widget in frame_devoluciones.winfo_children():
        widget.destroy()

    for i, libro in enumerate(libros):
        b = tk.Button(frame_devoluciones, text=f"Devolver '{libro.titulo}'", command=lambda idx=i: devolver_libro(idx), bg="#ffc107")
        b.pack(pady=2)
        devolver_botones.append(b)

def devolver_libro(index):
    msg = usuario1.prestamos[index].marcar_devolucion()
    area_salida.insert("end", msg + "\n")
    area_salida.insert("end", usuario1.mostrar_prestamo() + "\n")

def reiniciar():
    libros.clear()
    libros_entries.clear()
    prestamos_entries.clear()
    devolver_botones.clear()
    usuario1 = None
    for frame in [frame_libros, frame_prestamos, frame_devoluciones]:
        for widget in frame.winfo_children():
            widget.destroy()
    entry_cantidad.delete(0, "end")
    entry_nombre.delete(0, "end")
    entry_id.delete(0, "end")
    area_salida.delete("1.0", "end")
    messagebox.showinfo("Reinicio", "El programa ha sido reiniciado.")


# ---------- INTERFAZ ----------
ventana = tk.Tk()
ventana.title("📚 Sistema de Préstamos de Libros")
ventana.geometry("900x700")
ventana.config(bg="#f0f0f0")

libros = []
libros_entries = []
prestamos_entries = []
devolver_botones = []
usuario1 = None

# --- Cantidad de libros ---
frame_cantidad = tk.LabelFrame(ventana, text="📘 Cantidad de libros", bg="#f0f0f0")
frame_cantidad.pack(fill="x", padx=10, pady=5)

tk.Label(frame_cantidad, text="Cantidad de libros:").pack(side="left", padx=5)
entry_cantidad = tk.Entry(frame_cantidad, width=5)
entry_cantidad.pack(side="left", padx=5)
tk.Button(frame_cantidad, text="Registrar", bg="#007bff", fg="white", command=registrar_libros).pack(side="left", padx=5)

# --- Datos de libros dinámicos ---
frame_libros = tk.LabelFrame(ventana, text="📖 Datos de Libros", bg="#f0f0f0")
frame_libros.pack(fill="x", padx=10, pady=5)

# --- Datos de usuario ---
frame_usuario = tk.LabelFrame(ventana, text="👤 Datos del Usuario", bg="#f0f0f0")
frame_usuario.pack(fill="x", padx=10, pady=5)

tk.Label(frame_usuario, text="Nombre:").grid(row=0, column=0, padx=5, pady=2)
entry_nombre = tk.Entry(frame_usuario)
entry_nombre.grid(row=0, column=1, padx=5)

tk.Label(frame_usuario, text="ID Usuario:").grid(row=0, column=2, padx=5, pady=2)
entry_id = tk.Entry(frame_usuario)
entry_id.grid(row=0, column=3, padx=5)

tk.Button(frame_usuario, text="Confirmar Usuario y Libros", bg="#28a745", fg="white", command=registrar_usuario).grid(row=0, column=4, padx=10)

# --- Préstamos ---
frame_prestamos = tk.LabelFrame(ventana, text="📅 Préstamos", bg="#f0f0f0")
frame_prestamos.pack(fill="x", padx=10, pady=5)

# --- Devoluciones ---
frame_devoluciones = tk.LabelFrame(ventana, text="↩️ Devoluciones", bg="#f0f0f0")
frame_devoluciones.pack(fill="x", padx=10, pady=5)

# --- Área de salida ---
area_salida = tk.Text(ventana, height=15, width=100, wrap="word")
area_salida.pack(padx=10, pady=10)

# --- Botón reiniciar ---
tk.Button(ventana, text="Reiniciar", bg="#dc3545", fg="white", command=reiniciar).pack(pady=10)

ventana.mainloop()
