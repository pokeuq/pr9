def count_even_odd():
    numbers = []
    while True:
        user_input = input("Введите число (или 'end' для завершения): ")
        if user_input.lower() == 'end':
            break
        try:
            number = float(user_input)
            if number.is_integer():
                numbers.append(int(number))
        except ValueError:
            print("Ошибка: введите корректное число!")

    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = sum(1 for num in numbers if num % 2 != 0)

    print(f"Получившийся список: {numbers}")
    print(f"Чётных чисел: {even_count}, Нечётных чисел: {odd_count}")

if __name__ == "__main__":
    count_even_odd()
