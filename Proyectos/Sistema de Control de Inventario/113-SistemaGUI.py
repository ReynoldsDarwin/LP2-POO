import os
import time
from datetime import datetime
from abc import ABC, abstractmethod
from barcode import Code128
from barcode.writer import ImageWriter

# ==========================================
# PALETA DE COLORES Y ESTILOS (UI/UX)
# ==========================================
class UI:
    GOLD = '\033[93m'
    SKY = '\033[96m'
    VIBRANT_GREEN = '\033[92m'
    CRITICAL_RED = '\033[91m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def banner():
        print(f"{UI.PURPLE}{UI.BOLD}" + "═"*60)
        print(f"{'MALL INFINITY - SISTEMA DE ALMACÉN CENTRAL':^60}")
        print("═"*60 + f"{UI.RESET}")

# ==========================================
# S - SINGLE RESPONSIBILITY: ENTIDAD
# ==========================================
class Producto:
    def __init__(self, id_p: int, nombre: str, cantidad: int, precio: float):
        self.id = id_p
        self.nombre = nombre.upper()
        self.cantidad = cantidad
        self.precio = precio
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M")

# ==========================================
# SERVICIO EXTERNO: GENERADOR DE BARCODES (RUTAS DINÁMICAS)
# ==========================================
class BarcodeService:
    """Servicio especializado en generar códigos de barras en el directorio local."""
    @staticmethod
    def generar_archivo(id_p: int):
        try:
            # 1. Obtener la ruta absoluta de la carpeta donde está este script
            directorio_actual = os.path.dirname(os.path.abspath(__file__))
            
            # 2. Configurar el nombre del archivo y la ruta completa
            nombre_base = f"barcode_{id_p}"
            ruta_completa = os.path.join(directorio_actual, nombre_base)
            
            # 3. Generar el código (Code128 estándar)
            codigo = Code128(str(id_p).zfill(12), writer=ImageWriter())
            
            # 4. Guardar usando la ruta absoluta
            # Nota: .save no necesita la extensión .png, ImageWriter la añade
            path_final = codigo.save(ruta_completa)
            
            return path_final
        except Exception as e:
            raise RuntimeError(f"Fallo en hardware de impresión: {str(e)}")

# ==========================================
# O / L - OPEN-CLOSED & LISKOV SUBSTITUTION
# ==========================================
class Inventario(ABC):
    @abstractmethod
    def guardar(self, producto: Producto): pass
    
    @abstractmethod
    def actualizar(self, id_p: int, cantidad: int): pass
    
    @abstractmethod
    def obtener_lista(self) -> list: pass
    
    @abstractmethod
    def buscar_por_id(self, id_p: int) -> Producto: pass

class MallInventory(Inventario):
    def __init__(self):
        self._db = {}

    def guardar(self, p: Producto):
        if p.id in self._db:
            raise ValueError(f"SKU DUPLICADO: El ID {p.id} ya existe.")
        self._db[p.id] = p

    def actualizar(self, id_p: int, cantidad: int):
        if id_p not in self._db:
            raise KeyError("Producto no registrado.")
        target = self._db[id_p]
        if target.cantidad + cantidad < 0:
            raise ValueError(f"Stock insuficiente: Solo hay {target.cantidad} unidades.")
        target.cantidad += cantidad

    def obtener_lista(self):
        return sorted(self._db.values(), key=lambda x: x.id)

    def buscar_por_id(self, id_p: int) -> Producto:
        if id_p not in self._db:
            raise KeyError("Producto no encontrado en la base de datos.")
        return self._db[id_p]

# ==========================================
# I - INTERFACE SEGREGATION: DASHBOARD
# ==========================================
class Dashboard:
    @staticmethod
    def imprimir_tabla(productos):
        UI.clear()
        UI.banner()
        print(f"{UI.BOLD}{'ID':<8} {'PRODUCTO':<20} {'STOCK':<12} {'PRECIO':<12} {'ESTADO'}{UI.RESET}")
        print("─"*60)
        
        for p in productos:
            color = UI.VIBRANT_GREEN
            msg = "OK"
            if p.cantidad <= 5:
                color, msg = UI.CRITICAL_RED, "CRÍTICO"
            elif p.cantidad <= 15:
                color, msg = UI.GOLD, "ALERTA"

            print(f"{p.id:<8} {p.nombre:<20} {p.cantidad:<12} s/. {p.precio:<10.2f} {color}{msg}{UI.RESET}")

    @staticmethod
    def ficha_lectura(p: Producto):
        print(f"\n{UI.SKY}╔══════════════════════════════════════════════╗")
        print(f"║           DETALLE DE ESCANEO ÓPTICO          ║")
        print(f"╠══════════════════════════════════════════════╣")
        print(f"║ SKU: {p.id:<40} ║")
        print(f"║ ART: {p.nombre:<40} ║")
        print(f"║ PVP: s/. {p.precio:<36.2f} ║")
        print(f"║ QTY: {p.cantidad:<40} ║")
        print(f"╚══════════════════════════════════════════════╝{UI.RESET}")

# ==========================================
# D - DEPENDENCY INVERSION: CORE SYSTEM
# ==========================================
class SupermarketApp:
    def __init__(self, motor: Inventario):
        self.sistema = motor

    def ejecutar(self):
        while True:
            UI.clear()
            UI.banner()
            print(f" {UI.VIBRANT_GREEN}1. [REGISTRAR]{UI.RESET}   {UI.SKY}2. [ENTRADA]{UI.RESET}   {UI.GOLD}3. [VENTA]{UI.RESET}")
            print(f" {UI.PURPLE}4. [INVENTARIO]{UI.RESET}  {UI.BOLD}5. [ESCÁNER]{UI.RESET}   {UI.CRITICAL_RED}6. [SALIR]{UI.RESET}")
            
            op = input(f"\n{UI.BOLD}SISTEMA_MALL > {UI.RESET}")

            try:
                if op == "1":
                    id_p = int(input("SKU / Código: "))
                    nom = input("Nombre Comercial: ")
                    stk = int(input("Stock Inicial: "))
                    pre = float(input("Precio s/.: "))
                    
                    self.sistema.guardar(Producto(id_p, nom, stk, pre))
                    
                    # Generación de archivo físico
                    print(f"{UI.SKY}Procesando etiqueta física...{UI.RESET}")
                    ruta_img = BarcodeService.generar_archivo(id_p)
                    print(f"✅ Archivo guardado en: {UI.BOLD}{ruta_img}{UI.RESET}")
                    time.sleep(2)

                elif op in ["2", "3"]:
                    id_p = int(input("Ingrese Código: "))
                    cant = int(input("Cantidad: "))
                    self.sistema.actualizar(id_p, cant if op == "2" else -cant)
                    print(f"{UI.VIBRANT_GREEN}✔ Base de datos actualizada.{UI.RESET}")
                    time.sleep(1)

                elif op == "4":
                    Dashboard.imprimir_tabla(self.sistema.obtener_lista())
                    total = sum(p.cantidad * p.precio for p in self.sistema.obtener_lista())
                    print(f"\n{UI.BOLD}VALOR TOTAL EN ALMACÉN: s/. {total:,.2f}{UI.RESET}")
                    input(f"\n{UI.SKY}Presione ENTER para continuar...{UI.RESET}")

                elif op == "5":
                    id_scan = int(input("ESCANEANDO... (Ingrese ID): "))
                    prod = self.sistema.buscar_por_id(id_scan)
                    Dashboard.ficha_lectura(prod)
                    input(f"\n{UI.GOLD}ENTER para nueva lectura...{UI.RESET}")

                elif op == "6":
                    break
            except Exception as e:
                print(f"\n{UI.CRITICAL_RED}{UI.BOLD}‼ ERROR: {e}{UI.RESET}")
                time.sleep(2)

if __name__ == "__main__":
    mall_core = MallInventory()
    app = SupermarketApp(mall_core)
    app.ejecutar()