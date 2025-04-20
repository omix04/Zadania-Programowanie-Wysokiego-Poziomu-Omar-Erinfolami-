import json
import os
import sys

class AplikacjaMobilna:
    def __init__(self, nazwa, wersja, pobrania=0, plik_json='app.json'):
        self.nazwa = nazwa
        self.wersja = wersja
        self.pobrania = pobrania
        self.plik_json = plik_json

    def nowe_pobranie(self):
        self.pobrania += 1
        self.zapisz_do_pliku()

    def ile_pobran(self):
        return self.pobrania

    def zapisz_do_pliku(self):
        dane = {
            "nazwa": self.nazwa,
            "wersja": self.wersja,
            "pobrania": self.pobrania
        }
        with open(self.plik_json, 'w') as f:
            json.dump(dane, f, indent=4)

    @classmethod
    def z_json(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as f:
            dane = json.load(f)
        return cls(
            dane['nazwa'],
            dane['wersja'],
            dane.get('pobrania', 0),  
            plik_json=nazwa_pliku
        )

# Inicjalizacja, jeśli plik nie istnieje
plik_json = 'app.json'
if not os.path.exists(plik_json):
    dane = {
        "nazwa": "OmarFile",
        "wersja": "2.0",
        "pobrania": 0
    }
    with open(plik_json, 'w') as f:
        json.dump(dane, f, indent=4)

# Główna logika programu
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "pobierz":
        app = AplikacjaMobilna.z_json(plik_json)
        app.nowe_pobranie()
        print("Pobrano aplikację:", app.nazwa)
        print("Łączna liczba pobrań:", app.ile_pobran())
    else:
        print("Użycie: python zad1zaj1.py pobierz")
