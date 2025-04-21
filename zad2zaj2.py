class UserNotFoundError(Exception):
    pass

class WrongPasswordError(Exception):
    pass

class UserAuth:
    def __init__(self, users):
        self.users = users

    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError(f"Użytkownik '{username}' nie istnieje.")
        if self.users[username] != password:
            raise WrongPasswordError(f"Nieprawidłowe hasło dla użytkownika '{username}'.")
        print(f"✅ Zalogowano pomyślnie jako '{username}'")

# Program interaktywny
if __name__ == "__main__":
    users = {
        "admin": "1234",
        "user": "abcd",
        "test": "test123"
    }
    auth = UserAuth(users)

    print("🔐 Witaj w systemie logowania!")
    print("Aby zakończyć wpisz 'exit' jako login.\n")

    while True:
        username = input("Login: ")
        if username.lower() == 'exit':
            print("👋 Zakończono program.")
            break
        password = input("Hasło: ")

        try:
            auth.login(username, password)
        except UserNotFoundError as e:
            print(f"❌ {e}")
        except WrongPasswordError as e:
            print(f"❌ {e}")
        print() 
