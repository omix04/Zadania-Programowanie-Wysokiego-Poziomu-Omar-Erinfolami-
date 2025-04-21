class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        return self.score == other.score

    def __ne__(self, other):
        return self.score != other.score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        return f"{self.name} (wynik: {self.score})"

def wczytaj_studenta(nr):
    print(f"\nPodaj dane dla studenta {nr}:")
    name = input("Imię: ")
    score = int(input("Wynik egzaminu: "))
    return Student(name, score)

if __name__ == "__main__":
    s1 = wczytaj_studenta(1)
    s2 = wczytaj_studenta(2)

    print("\nPorównanie studentów:")
    print(s1)
    print(s2)

    if s1 > s2:
        print(f"\n{s1.name} ma wyższy wynik niż {s2.name}.")
    elif s1 < s2:
        print(f"\n{s2.name} ma wyższy wynik niż {s1.name}.")
    else:
        print(f"\n{s1.name} i {s2.name} mają taki sam wynik.")
