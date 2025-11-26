class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, escalar):
        return Vector2D(self.x * escalar, self.y * escalar)

    def __str__(self):
        return f"({self.x}, {self.y})"

def main():
    v1 = Vector2D(2, 4)
    v2 = Vector2D(3, 1)

    suma = v1 + v2
    resta = v1 - v2
    multiplicacion = v1 * 3 

    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    print("-" * 20)
    print(f"Suma (v1 + v2): {suma}")
    print(f"Resta (v1 - v2): {resta}")
    print(f"Multiplicación escalar (v1 * 3): {multiplicacion}")

if __name__ == "__main__":
    main()