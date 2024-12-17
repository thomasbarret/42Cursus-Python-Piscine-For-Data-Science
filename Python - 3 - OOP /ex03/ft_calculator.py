class calculator:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, scalar) -> None:
        """Additionne un scalaire à chaque élément du vecteur"""
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)

    def __mul__(self, scalar) -> None:
        """Multiplie chaque élément du vecteur par un scalaire"""
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)

    def __sub__(self, scalar) -> None:
        """Soustrait un scalaire à chaque élément du vecteur"""
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)

    def __truediv__(self, scalar) -> None:
        """Divise chaque élément du vecteur par un scalaire.
        Si le scalaire est 0, afficher un message d'erreur."""
        if scalar == 0:
            print("Error: Division by zero.")
        else:
            self.vector = [x / scalar for x in self.vector]
            print(self.vector)
