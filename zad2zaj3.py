from typing import List

def average(numbers: List[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    print("Podaj liczby oddzielone spacją:")
    wejscie = input("")

    try:
        liczby = [float(x) for x in wejscie.strip().split()]
        wynik = average(liczby)
        print(f"Średnia: {wynik}")
    except ValueError:
        print("Podano nieprawidłowe dane. Upewnij się, że wpisujesz liczby zmiennoprzecinkowe.")
