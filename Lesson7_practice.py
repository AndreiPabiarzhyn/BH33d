class User:
        def __init__(self, name: str, email: str) -> None:
            self. first_name = name.title()
            self. email = email.lower()

vasya = User(
    name='vasya',
    email='vasya@info.com'
)
print(vasya.email)
