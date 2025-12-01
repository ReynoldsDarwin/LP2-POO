import math
import customtkinter as ctk

# Configuración inicial del tema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class HipotenusaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora de Hipotenusa")
        self.geometry("400x480") # Aumenté un poco la altura por si el error es largo
        self.resizable(False, False)

        self.setup_ui()

    def setup_ui(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        self.lbl_title = ctk.CTkLabel(
            self, 
            text="Cálculo Geométrico", 
            font=("Roboto Medium", 24)
        )
        self.lbl_title.pack(pady=(40, 20))

        self.entry_a = ctk.CTkEntry(
            self, 
            placeholder_text="Cateto A", 
            width=250,
            height=40,
            font=("Roboto", 14)
        )
        self.entry_a.pack(pady=10)

        self.entry_b = ctk.CTkEntry(
            self, 
            placeholder_text="Cateto B", 
            width=250,
            height=40,
            font=("Roboto", 14)
        )
        self.entry_b.pack(pady=10)

        self.btn_calcular = ctk.CTkButton(
            self, 
            text="Calcular Hipotenusa", 
            command=self.calcular,
            width=250,
            height=45,
            font=("Roboto", 15, "bold"),
            fg_color="#1F6AA5",
            hover_color="#144870"
        )
        self.btn_calcular.pack(pady=(20, 10))

        self.lbl_resultado = ctk.CTkLabel(
            self, 
            text="", 
            font=("Roboto", 16),
            text_color="#FFFFFF",
            wraplength=350  # Permite que el texto baje de línea si el error es largo
        )
        self.lbl_resultado.pack(pady=20)

    def calcular_hipotenusa(self, a: float, b: float) -> float:
        # math.hypot maneja mejor el desbordamiento que sqrt(a**2 + b**2)
        return math.hypot(a, b)

    def calcular(self) -> None:
        try:
            val_a = self.entry_a.get()
            val_b = self.entry_b.get()

            # Validación de campos vacíos
            if not val_a or not val_b:
                self.lbl_resultado.configure(text="Error: Campos vacíos", text_color="#FF5555")
                return

            a = float(val_a)
            b = float(val_b)

            # Validación de lógica de negocio (números positivos)
            if a <= 0 or b <= 0:
                self.lbl_resultado.configure(text="Error: Use números positivos", text_color="#FF5555")
                return

            resultado = self.calcular_hipotenusa(a, b)
            
            # Éxito
            self.lbl_resultado.configure(text=f"Hipotenusa: {resultado:.2f}", text_color="#2CC985")

        except ValueError:
            # Captura errores de conversión (ej: letras)
            self.lbl_resultado.configure(text="Error: Entrada no numérica", text_color="#FF5555")

        except OverflowError:
            # Captura si el número es demasiado grande para Python
            self.lbl_resultado.configure(text="Error: Número demasiado grande", text_color="#FF5555")

        except Exception as e:
            # Captura CUALQUIER otro error inesperado y lo muestra en la UI
            self.lbl_resultado.configure(text=f"Error inesperado: {str(e)}", text_color="#FF5555")

def main() -> None:
    app = HipotenusaApp()
    app.mainloop()

if __name__ == "__main__":
    main()