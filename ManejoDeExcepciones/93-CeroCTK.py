import customtkinter as ctk

# Clase para manejar la división con manejo de excepciones
class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def dividir(self):
        try:
            resultado = self.a / self.b
            return f"Resultado: {resultado}"
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero."
        except Exception as e:
            return f"Ocurrió un error: {e}"
        finally:
            print("Operación finalizada")


# --- Interfaz gráfica ---
def realizar_division():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        operacion = Division(a, b)
        resultado_label.configure(text=operacion.dividir())
    except ValueError:
        resultado_label.configure(text="Error: ingrese solo números.")


# Configuración inicial de la ventana
ctk.set_appearance_mode("dark")   # 'dark' o 'light'
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("División con manejo de excepciones")
ventana.geometry("400x300")

# --- Widgets ---
titulo = ctk.CTkLabel(ventana, text="División de dos números", font=("Arial", 20, "bold"))
titulo.pack(pady=15)

frame_inputs = ctk.CTkFrame(ventana)
frame_inputs.pack(pady=10)

label_a = ctk.CTkLabel(frame_inputs, text="Número A:")
label_a.grid(row=0, column=0, padx=10, pady=5)
entry_a = ctk.CTkEntry(frame_inputs, width=150)
entry_a.grid(row=0, column=1, padx=10, pady=5)

label_b = ctk.CTkLabel(frame_inputs, text="Número B:")
label_b.grid(row=1, column=0, padx=10, pady=5)
entry_b = ctk.CTkEntry(frame_inputs, width=150)
entry_b.grid(row=1, column=1, padx=10, pady=5)

btn_dividir = ctk.CTkButton(ventana, text="Dividir", command=realizar_division)
btn_dividir.pack(pady=10)

resultado_label = ctk.CTkLabel(ventana, text="", font=("Arial", 14))
resultado_label.pack(pady=10)

# Iniciar ventana
ventana.mainloop()
