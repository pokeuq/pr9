def shift_right(numbers):
  if len(numbers) > 0:
      last_element = numbers[-1]
      for i in range(len(numbers) - 1, 0, -1):
          numbers[i] = numbers[i - 1]
      numbers[0] = last_element
  print(f"Циклически сдвинутый список: {numbers}")

if __name__ == "__main__":
  numbers = input("Введите список чисел через пробел: ").split()

  try:
      numbers = [int(x) for x in numbers]
  except ValueError:
      print("Ошибка: Введите только целые числа.")
  else:
      shift_right(numbers)
def shift_right(numbers):
    if len(numbers) == 0:
        print("Список пустой.")
        return
    if len(numbers) == 1:
        print("Список содержит только один элемент, сдвиг не требуется.")
        return

    last_element = numbers[-1]
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1]
    numbers[0] = last_element
    print(f"Циклически сдвинутый список: {numbers}")

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
            shift_right(numbers)
