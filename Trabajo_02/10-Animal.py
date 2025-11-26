from abc import ABC, abstractmethod
from typing import List

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau!")

def main():
    animales: List[Animal] = [
        Perro(),
        Gato(),
        Perro()
    ]

    for animal in animales:
        animal.hacer_sonido()

if __name__ == "__main__":
    main()