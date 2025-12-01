import tkinter as tk
from tkinter import font as tkfont

# --- Configuración de Colores ---
COLOR_FONDO = "#202020"
COLOR_INPUT = "#333333"
COLOR_TEXTO = "#FFFFFF"
COLOR_BOTON = "#0078D7"
COLOR_ERROR = "#FF5555"  # Rojo brillante para errores
COLOR_EXITO = "#4CC9F0"  # Cian para éxito

class FibonacciApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora Fibonacci")
        self.geometry("400x400")
        self.resizable(False, False)
        self.configure(bg=COLOR_FONDO)

        self.crear_interfaz()

    def crear_interfaz(self):
        # 1. Título
        tk.Label(
            self, text="Fibonacci Checker", 
            font=("Segoe UI", 20, "bold"),
            bg=COLOR_FONDO, fg=COLOR_TEXTO
        ).pack(pady=(40, 20))

        # 2. Entrada de datos
        self.entrada = tk.Entry(
            self, 
            font=("Segoe UI", 14), 
            bg=COLOR_INPUT, fg=COLOR_TEXTO,
            insertbackground="white", relief="flat", justify="center"
        )
        self.entrada.pack(pady=10, ipady=5, padx=50)
        self.entrada.focus() # Poner el cursor aquí al iniciar

        # 3. Botón
        tk.Button(
            self, text="CALCULAR",
            command=self.procesar,
            font=("Segoe UI", 12, "bold"),
            bg=COLOR_BOTON, fg="white",
            relief="flat", cursor="hand2", activebackground="#005a9e"
        ).pack(pady=20, ipadx=20, ipady=5)

        # 4. ETIQUETA DE ERROR / RESULTADO (Aquí se mostrará el mensaje)
        self.lbl_feedback = tk.Label(
            self, 
            text="", # Empieza vacía
            font=("Segoe UI", 12),
            bg=COLOR_FONDO, 
            fg=COLOR_TEXTO,
            wraplength=350 # Para que el texto baje si es muy largo
        )
        self.lbl_feedback.pack(pady=20)

    def calcular_fibonacci(self, n):
        if n < 0:
            raise ValueError("El número no puede ser negativo.")
        if n > 10000: # Límite por seguridad
             raise OverflowError("Número demasiado grande (max 10,000).")
        if n == 0: return 0
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def procesar(self):
        valor = self.entrada.get()
        
        try:
            # 1. Validar que no esté vacío
            if not valor:
                raise ValueError("El campo está vacío.")

            # 2. Validar que sea número
            try:
                n = int(valor)
            except ValueError:
                raise ValueError("Debes ingresar un número entero.")

            # 3. Calcular
            resultado = self.calcular_fibonacci(n)

            # 4. MOSTRAR ÉXITO EN LA VENTANA
            # Cambiamos el color a Azul/Cian y mostramos el resultado
            self.lbl_feedback.config(
                text=f"Fibonacci({n}) = {resultado}", 
                fg=COLOR_EXITO
            )

        except Exception as e:
            # 5. MOSTRAR ERROR EN LA VENTANA
            # Cambiamos el color a Rojo y mostramos la excepción
            self.lbl_feedback.config(
                text=f"⚠ ERROR: {str(e)}", 
                fg=COLOR_ERROR
            )

if __name__ == "__main__":
    app = FibonacciApp()
    app.mainloop()