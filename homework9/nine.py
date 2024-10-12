import re

def parse_email(email):
    email = email.strip()

    if not email:
        print("Ошибка: email не может быть пустым.")
        return

    pattern = r"([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    match = re.match(pattern, email)

    if match:
        username, domain = match.groups()
        print(f"Username: {username}, Domain: {domain}")
    else:
        print("Ошибка: некорректный email.")

if __name__ == "__main__":
    email = input("Введите email: ")
    parse_email(email)
