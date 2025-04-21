from typing import List

class SimpleChatbot:
    def __init__(self, questions: List[str]):
        self.questions = questions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.index < len(self.questions):
            question = self.questions[self.index]
            self.index += 1
            return question
        else:
            raise StopIteration
        
if __name__ == "__main__":
    bot = SimpleChatbot([
        "Jak się nazywasz?",
        "Jaki jest Twój ulubiony kolor?",
        "Co lubisz robić w wolnym czasie?"
    ])

    for question in bot:
        print("", question)
        input("Odpowiedź: ")
