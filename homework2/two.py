import math

def squares_between(a: float, b: float):
    try:

        start = math.ceil(min(a, b))
        end = math.floor(max(a, b)) 

        if start <= end:
            return [i**2 for i in range(start, end + 1)]
        else:
            return []
    except ValueError:
        print("Ошибка: Введите корректные числа!")

def main():
    try:
        a = float(input("Введите число a: "))  
        b = float(input("Введите число b: "))
        result = squares_between(a, b)

        if result:
            print(f"Квадраты чисел между {a} и {b}: {result}")
        else:
            print(f"Между {a} и {b} нет целых чисел.")
    except ValueError:
        print("Ошибка: Введите корректные числа!")

if __name__ == "__main__":
    main()
