class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
    
    def opis(self):
        return f"'{self.tytul}' autorstwa {self.autor}, wydana w {self.rok_wydania}."

class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku
    
    def opis(self):
        podstawowy_opis = super().opis()
        return f"{podstawowy_opis} Rozmiar pliku: {self.rozmiar_pliku} MB."


class Audiobook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, czas_trwania):
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania = czas_trwania
    
    def opis(self):
        podstawowy_opis = super().opis()
        return f"{podstawowy_opis} Czas trwania: {self.czas_trwania} minut."


ksiazka1 = Ksiazka("Mistrz i Małgorzata", "Michaił Bułhakow", 1967)
ebook1 = Ebook("Harry Potter i Kamień Filozoficzny", "J.K. Rowling", 1997, 5.4)
audiobook1 = Audiobook("Władca Pierścieni: Drużyna Pierścienia", "J.R.R. Tolkien", 1954, 720)

print(ksiazka1.opis())       
print(ebook1.opis())         
print(audiobook1.opis())     
