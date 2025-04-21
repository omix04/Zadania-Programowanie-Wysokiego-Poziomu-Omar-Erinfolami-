from typing import Dict, Optional

class Library:
    def __init__(self):
        self.books: Dict[str, str] = {}

    def add_book(self, isbn: str, title: str) -> None:
        self.books[isbn] = title

    def find_book(self, isbn: str) -> Optional[str]:
        return self.books.get(isbn)

if __name__ == "__main__":
    biblioteka = Library()
    
    print("Dodawanie książek do biblioteki.")
    print("Wpisz 'koniec' jako ISBN, aby zakończyć dodawanie.\n")

    while True:
        isbn = input("Podaj ISBN: ").strip()
        if isbn.lower() == "koniec":
            break
        title = input("Podaj tytuł: ").strip()
        biblioteka.add_book(isbn, title)
        print("Dodano książkę!\n")

    print("\nWyszukiwanie książki:")
    isbn_szukaj = input("Podaj numer ISBN książki, której szukasz: ").strip()
    wynik = biblioteka.find_book(isbn_szukaj)

    if wynik:
        print(f"Tytuł: {wynik}")
    else:
        print("Nie znaleziono książki o podanym ISBN.")

