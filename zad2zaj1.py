class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        return Matrix(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d
        )

    def __mul__(self, other):
        return Matrix(
            self.a * other.a + self.b * other.c,
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d
        )

    def __str__(self):
        return f"[{self.a}, {self.b};\n {self.c}, {self.d}]"

    def __repr__(self):
        return f"Matrix({self.a}, {self.b}, {self.c}, {self.d})"

def wczytaj_macierz(nr):
    print(f"\nPodaj dane dla macierzy {nr}:")
    a = int(input("Element a "))
    b = int(input("Element b "))
    c = int(input("Element c "))
    d = int(input("Element d "))
    return Matrix(a, b, c, d)

if __name__ == "__main__":
    m1 = wczytaj_macierz(1)
    m2 = wczytaj_macierz(2)

    print("\nMacierz 1:")
    print(m1)
    print("\nMacierz 2:")
    print(m2)

    suma = m1 + m2
    iloczyn = m1 * m2

    print("\nSuma macierzy:")
    print(suma)

    print("\nIloczyn macierzy:")
    print(iloczyn)

    print("\nReprezentacja iloczynu:")
    print(repr(iloczyn))
