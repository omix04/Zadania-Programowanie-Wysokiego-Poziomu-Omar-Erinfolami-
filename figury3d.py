import math

def objetosc_szescianu(bok: float) -> float:
    return bok ** 3

def pole_szescianu(bok: float) -> float:
    return 6 * bok ** 2

def objetosc_prostopadloscianu(a: float, b: float, h: float) -> float:
    return a * b * h

def pole_prostopadloscianu(a: float, b: float, h: float) -> float:
    return 2 * (a * b + a * h + b * h)

def objetosc_kuli(promien: float) -> float:
    return (4/3) * math.pi * promien ** 3

def pole_kuli(promien: float) -> float:
    return 4 * math.pi * promien ** 2

print("\n=== 3D ===")
print("Objętość kuli (r=2):", objetosc_kuli(2))
print("Pole prostopadłościanu (2x3x4):", pole_prostopadloscianu(2, 3, 4))
print("Objętość sześcianu (bok=5):", objetosc_szescianu(5))