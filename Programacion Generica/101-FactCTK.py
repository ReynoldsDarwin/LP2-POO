import sys
import customtkinter as ctk
from typing import Generic, TypeVar

# Configuración para permitir imprimir números gigantes
sys.set_int_max_str_digits(0)

T = TypeVar('T', int, float)

class CalculadoraFactorial(Generic[T]):
    def __init__(self, numero: T):
        self.numero = numero
        
    def calcular_factorial(self) -> int:
        n = int(self.numero)
        if n < 0:
            raise ValueError("El factorial no está definido para negativos.")
        
        # Límite de seguridad para evitar congelamiento de la GUI
        if n > 20000:
            raise OverflowError("El número es demasiado alto para esta demo (Límite: 20,000).")

        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class FactorialApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora Factorial")
        self.geometry("500x550")
        self.resizable(False, False)

        self.setup_ui()

    def setup_ui(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.lbl_title = ctk.CTkLabel(
            self, 
            text="Cálculo Factorial (n!)", 
            font=("Roboto Medium", 24)
        )
        self.lbl_title.grid(row=0, column=0, pady=(35, 20), sticky="ew")

        self.entry_n = ctk.CTkEntry(
            self, 
            placeholder_text="Ingrese número entero (ej: 50)", 
            width=300,
            height=40,
            font=("Roboto", 14)
        )
        self.entry_n.grid(row=1, column=0, pady=10)

        self.btn_calcular = ctk.CTkButton(
            self, 
            text="Calcular Factorial", 
            command=self.ejecutar_calculo,
            width=300,
            height=45,
            font=("Roboto", 15, "bold"),
            fg_color="#1F6AA5",
            hover_color="#144870"
        )
        self.btn_calcular.grid(row=2, column=0, pady=(15, 10))

        self.lbl_status = ctk.CTkLabel(
            self,
            text="Resultado:",
            font=("Roboto", 12),
            text_color="#AAAAAA"
        )
        self.lbl_status.grid(row=3, column=0, pady=(10, 5), padx=40, sticky="w")

        self.txt_output = ctk.CTkTextbox(
            self,
            width=420,
            height=200,
            font=("Consolas", 13),
            corner_radius=10
        )
        self.txt_output.grid(row=4, column=0, pady=(0, 30), padx=20, sticky="nsew")
        self.txt_output.configure(state="disabled")

    def mostrar_mensaje(self, mensaje: str, es_error: bool = False) -> None:
        self.txt_output.configure(state="normal")
        self.txt_output.delete("0.0", "end")
        
        if es_error:
            self.txt_output.insert("0.0", f"⚠ ERROR:\n{mensaje}")
            self.txt_output.configure(text_color="#FF5555")
        else:
            self.txt_output.insert("0.0", mensaje)
            self.txt_output.configure(text_color="#FFFFFF")
            
        self.txt_output.configure(state="disabled")

    def ejecutar_calculo(self) -> None:
        entrada = self.entry_n.get()
        
        try:
            if not entrada:
                raise ValueError("El campo está vacío.")

            try:
                val = float(entrada) 
                if not val.is_integer():
                    raise ValueError("El factorial solo se define para enteros.")
                n = int(val)
            except ValueError:
                raise ValueError("Debe ingresar un número válido.")

            calc = CalculadoraFactorial(n)
            resultado = calc.calcular_factorial()
            
            self.mostrar_mensaje(str(resultado))

        except ValueError as ve:
            self.mostrar_mensaje(str(ve), es_error=True)
        except OverflowError as oe:
            self.mostrar_mensaje(str(oe), es_error=True)
        except Exception as e:
            self.mostrar_mensaje(f"Error inesperado: {e}", es_error=True)

if __name__ == "__main__":
    app = FactorialApp()
    app.mainloop()