import math

def pole_kwadratu(bok: float) -> float:
    return bok * bok

def obwod_kwadratu(bok: float) -> float:
    return 4 * bok

def pole_prostokata(a: float, b: float) -> float:
    return a * b

def obwod_prostokata(a: float, b: float) -> float:
    return 2 * (a + b)

def pole_kola(promien: float) -> float:
    return math.pi * promien ** 2

def obwod_kola(promien: float) -> float:
    return 2 * math.pi * promien

print("=== 2D ===")
print("Pole kwadratu (bok=4):", pole_kwadratu(4))
print("Obwód koła (r=3):", obwod_kola(3))
print("Pole prostokąta (3x5):", pole_prostokata(3, 5))