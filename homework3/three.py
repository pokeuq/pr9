def get_odd_numbers():
    numbers = []
    while True:
        user_input = input("Введите число (или 'end' для завершения): ")
        if user_input.lower() == 'end':
            break
        try:
            number = float(user_input)  # Позволяем вводить вещественные числа
            if number.is_integer():
                if int(number) % 2 != 0:
                    numbers.append(int(number))
        except ValueError:
            print("Ошибка: введите корректное число!")

    print(f"Нечетные числа: {numbers}")

if __name__ == "__main__":
    get_odd_numbers()
