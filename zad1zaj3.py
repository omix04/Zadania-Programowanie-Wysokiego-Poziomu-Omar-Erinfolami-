#wybrałem Kompozycje ponieważ Wielodziedziczenie mogłoby prowadzić do konfliktów nazw 
#metod w więcej niż jednej klasie

# Klasa bazowa Asystent
class Asystent:
    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja

# Klasa odpowiedzialna za analizę językową
class AnalizaJezykowa:
    def analizuj_zapytanie(self, zapytanie):
        if "pogoda" in zapytanie.lower():
            return "intencja: pogoda"
        elif "czas" in zapytanie.lower():
            return "intencja: czas"
        else:
            return "intencja: ogólna"

# Klasa odpowiedzialna za generowanie odpowiedzi
class GeneratorOdpowiedzi:
    def generuj_odpowiedz(self, analiza):
        if "pogoda" in analiza:
            return "Dzisiaj jest słonecznie i 22°C."
        elif "czas" in analiza:
            return "Aktualna godzina to 14:30."
        else:
            return "Przepraszam, nie zrozumiałem pytania."

# Klasa łącząca funkcjonalności – KOMPOZYCJA
class InteligentnyAsystent:
    def __init__(self, nazwa, wersja):
        self.asystent = Asystent(nazwa, wersja)
        self.analizator = AnalizaJezykowa()
        self.generator = GeneratorOdpowiedzi()

    def odpowiedz_na_zapytanie(self, zapytanie):
        analiza = self.analizator.analizuj_zapytanie(zapytanie)
        odpowiedz = self.generator.generuj_odpowiedz(analiza)
        print(f"[{self.asystent.nazwa} v{self.asystent.wersja}] → {odpowiedz}")

if __name__ == "__main__":
    bot = InteligentnyAsystent("LingoBot", "1.0")

    while True:
        pytanie = input("Zadaj pytanie ('exit' aby zakończyć): ")
        if pytanie.lower() == "exit":
            print("👋 Do zobaczenia!")
            break
        bot.odpowiedz_na_zapytanie(pytanie)