def find_factors(n, factor=2):
    if n <= 1:
        return []
    if n % factor == 0:
        return [factor] + find_factors(n // factor, factor)
    else:
        return find_factors(n, factor + 1)

try:
    n = int(input("Введіть число: "))
    if n <= 0:
        raise ValueError("Число повинно бути більше нуля")
    factors = find_factors(n)
    print(f"Множники числа {n}: {'*'.join(map(str, factors))}")
except ValueError as e:
    print(f"Помилка: {e}")
except Exception as e:
    print(f"Несподівана помилка: {e}")
finally:
    print("Програма завершена")
