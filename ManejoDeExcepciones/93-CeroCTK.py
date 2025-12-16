import customtkinter as ctk
from tkinter import messagebox


# ================== CLASE ORIGINAL ==================
class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dividir(self):
        try:
            resultado = self.a / self.b
            return resultado
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero"
        except Exception as e:
            return f"Ocurrió un error: {e}"
        finally:
            print("Operación finalizada")


# ================== INTERFAZ GRÁFICA ==================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("➗ División segura")
ventana.geometry("420x350")

ctk.CTkLabel(
    ventana,
    text="➗ DIVISIÓN CON MANEJO DE ERRORES",
    font=("Segoe UI", 20, "bold")
).pack(pady=20)

frame = ctk.CTkFrame(ventana, corner_radius=15)
frame.pack(padx=20, pady=15, fill="x")

ctk.CTkLabel(frame, text="Valor A:", font=("Segoe UI", 14)).pack(pady=(15, 5))
entry_a = ctk.CTkEntry(frame, placeholder_text="Ingrese el primer número")
entry_a.pack(pady=5)

ctk.CTkLabel(frame, text="Valor B:", font=("Segoe UI", 14)).pack(pady=(15, 5))
entry_b = ctk.CTkEntry(frame, placeholder_text="Ingrese el segundo número")
entry_b.pack(pady=5)

label_resultado = ctk.CTkLabel(
    ventana,
    text="Resultado: ---",
    font=("Consolas", 16, "bold"),
    text_color="#CCCCCC"
)
label_resultado.pack(pady=20)


# ================== FUNCIÓN DEL BOTÓN ==================
def realizar_division():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Error", "Debe ingresar números válidos.")
        return

    operacion = Division(a, b)
    resultado = operacion.dividir()

    if isinstance(resultado, str):
        label_resultado.configure(text=resultado, text_color="#FF6B6B")
    else:
        label_resultado.configure(
            text=f"Resultado: {resultado}",
            text_color="#4CAF50"
        )


# ================== BOTÓN ==================
ctk.CTkButton(
    ventana,
    text="Calcular división",
    width=200,
    height=40,
    command=realizar_division
).pack(pady=10)

ctk.CTkLabel(
    ventana,
    text="La operación se finaliza siempre (bloque finally)",
    font=("Segoe UI", 11, "italic"),
    text_color="#888888"
).pack(pady=10)

ventana.mainloop()
