from typing import Generator

def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    n = int(input("Ile liczb Fibonacciego wyświetlić? "))

    print("Ciąg Fibonacciego:")
    gen = fibonacci()
    for _ in range(n):
        print(next(gen), end=" ")