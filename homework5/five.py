def print_greater_than_previous(numbers):
    result = []
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            result.append(numbers[i])
    print(f"Числа больше предыдущего: {result}")

if __name__ == "__main__":
    numbers = input("Введите список чисел через пробел: ").split()

    try:
        numbers = [float(x) for x in numbers]
    except ValueError:
        print("Ошибка: Введите только числа.")
    else:
        print_greater_than_previous(numbers)
