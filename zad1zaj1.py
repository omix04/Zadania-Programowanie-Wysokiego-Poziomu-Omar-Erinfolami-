import json
import os

class AplikacjaMobilna:
    liczba_pobran = 0

    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja

    def nowe_pobranie(self):
        AplikacjaMobilna.liczba_pobran += 1

    @classmethod
    def ile_pobran(cls):
        return cls.liczba_pobran

    @classmethod
    def z_json(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as f:
            dane = json.load(f)
        return cls(dane['nazwa'], dane['wersja'])

plik_json = 'app.json'
if not os.path.exists(plik_json):
    dane = {
        "nazwa": "OmarFile",
        "wersja": "2.0"
    }
    with open(plik_json, 'w') as f:
        json.dump(dane, f, indent=4)

# Użycie klasy
app = AplikacjaMobilna.z_json(plik_json)
print("Nazwa aplikacji:", app.nazwa)
print("Wersja:", app.wersja)

# Symulacja pobrań
app.nowe_pobranie()
app.nowe_pobranie()
app.nowe_pobranie()

print("Liczba pobrań:", AplikacjaMobilna.ile_pobran())
