def swap_min_max(numbers):
    if len(numbers) == 0:
        print("Список пустой.")
        return
    if len(numbers) == 1:
        print("Список содержит только одно число, менять нечего.")
        return

    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))

    if min_index == max_index:
        print("Минимальный и максимальный элемент одинаковы, менять нечего.")
    else:
        numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
        print(f"Изменённый список: {numbers}")

if __name__ == "__main__":
    numbers = input("Введите список чисел через пробел: ").split()

    if not numbers:
        print("Ошибка: Введён пустой список.")
    else:
        try:
            numbers = [float(x) for x in numbers]
        except ValueError:
            print("Ошибка: Введите только корректные числа.")
        else:
            swap_min_max(numbers)
