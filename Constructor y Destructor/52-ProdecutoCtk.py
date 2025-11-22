import customtkinter as ctk
import gc

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        return f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.cantidad}"

    def __del__(self):
        print(f"Producto eliminado: {self.nombre}")  # se muestra en consola


# --- Funciones de la interfaz ---
def registrar_producto():
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    cantidad = entry_cantidad.get()

    if not nombre or not precio or not cantidad:
        salida.insert("end", "⚠️ Por favor completa todos los campos.\n")
        return

    try:
        precio = float(precio)
        cantidad = int(cantidad)
    except ValueError:
        salida.insert("end", "⚠️ Precio debe ser número decimal y cantidad un entero.\n")
        return

    producto = Producto(nombre, precio, cantidad)
    productos.append(producto)
    salida.insert("end", f"Producto registrado: {nombre} - ${precio:.2f} en stock {cantidad}\n")

    entry_nombre.delete(0, "end")
    entry_precio.delete(0, "end")
    entry_cantidad.delete(0, "end")

def mostrar_informacion():
    if not productos:
        salida.insert("end", "⚠️ No hay productos registrados.\n")
        return
    salida.insert("end", "\n--- Información de productos ---\n")
    for producto in productos:
        salida.insert("end", producto.mostrar_informacion() + "\n")

def eliminar_productos():
    global productos
    if not productos:
        salida.insert("end", "⚠️ No hay productos para eliminar.\n")
        return
    productos.clear()
    gc.collect()
    salida.insert("end", "\n⚠️ Productos eliminados.\nFin del programa.\n")

def reiniciar_programa():
    global productos
    productos.clear()
    gc.collect()
    entry_nombre.delete(0, "end")
    entry_precio.delete(0, "end")
    entry_cantidad.delete(0, "end")
    salida.delete("1.0", "end")
    salida.insert("end", "🔄 Programa reiniciado.\n")


# --- Configuración ventana ---
ctk.set_appearance_mode("dark")   # "light" o "dark"
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Gestión de Productos")
ventana.geometry("600x520")
ventana.resizable(False, False)

productos = []

# --- Título ---
titulo = ctk.CTkLabel(ventana, text="Gestión de Productos", font=("Segoe UI", 20, "bold"))
titulo.pack(pady=15)

# --- Entradas ---
frame_inputs = ctk.CTkFrame(ventana, corner_radius=12)
frame_inputs.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(frame_inputs, text="Nombre del producto:", font=("Segoe UI", 13)).pack(pady=5)
entry_nombre = ctk.CTkEntry(frame_inputs, placeholder_text="Ejemplo: Pan")
entry_nombre.pack(pady=5, padx=10, fill="x")

ctk.CTkLabel(frame_inputs, text="Precio:", font=("Segoe UI", 13)).pack(pady=5)
entry_precio = ctk.CTkEntry(frame_inputs, placeholder_text="Ejemplo: 10.50")
entry_precio.pack(pady=5, padx=10, fill="x")

ctk.CTkLabel(frame_inputs, text="Stock:", font=("Segoe UI", 13)).pack(pady=5)
entry_cantidad = ctk.CTkEntry(frame_inputs, placeholder_text="Ejemplo: 20")
entry_cantidad.pack(pady=5, padx=10, fill="x")

# --- Botones ---
frame_botones = ctk.CTkFrame(ventana, fg_color="transparent")
frame_botones.pack(pady=15)

btn_registrar = ctk.CTkButton(frame_botones, text="Registrar", command=registrar_producto)
btn_registrar.grid(row=0, column=0, padx=10)

btn_mostrar = ctk.CTkButton(frame_botones, text="Mostrar información", command=mostrar_informacion)
btn_mostrar.grid(row=0, column=1, padx=10)

btn_eliminar = ctk.CTkButton(frame_botones, text="Eliminar", command=eliminar_productos)
btn_eliminar.grid(row=0, column=2, padx=10)

btn_reiniciar = ctk.CTkButton(frame_botones, text="Reiniciar", command=reiniciar_programa, fg_color="#d9534f", hover_color="#c9302c")
btn_reiniciar.grid(row=0, column=3, padx=10)

# --- Área de salida ---
salida = ctk.CTkTextbox(ventana, width=560, height=200, wrap="word", font=("Consolas", 12))
salida.pack(pady=15, padx=20)

ventana.mainloop()
