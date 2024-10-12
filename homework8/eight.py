import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def user_choice():
    user_numbers = []
    selected_numbers = set()
    for row in ticket:
        print(f"Ряд: {row}")
        while True:
            try:
                num = input(f"Выберите число из ряда {row}: ")
                if num.lower() == "exit":
                    print("Выход из программы.")
                    return user_numbers 
                num = int(num)

                if num in row:
                    if num not in selected_numbers:
                        user_numbers.append(num)
                        selected_numbers.add(num) 
                        break
                    else:
                        print("Ошибка: Вы уже выбрали это число, выберите другое.")
                else:
                    print(f"Ошибка: Число должно быть одним из ряда {row}.")
            except ValueError:
                print("Ошибка: введите корректное целое число.")
    return user_numbers

def lottery():
    random_numbers = [random.choice(row) for row in ticket]
    return random_numbers

if __name__ == "__main__":
    user_numbers = user_choice()

    if len(user_numbers) < len(ticket):
        print("Ошибка: Не выбрано достаточное количество чисел.")
    else:
        random_numbers = lottery()
        print('')
        print(f"Ваши числа: {user_numbers}")
        print(f"Выигрышные числа: {random_numbers}")
        matches = set(user_numbers) & set(random_numbers)
        if matches:
            print(f"Совпадения: {list(matches)}")
        else:
            print(f"Совпадений нет :(")  
