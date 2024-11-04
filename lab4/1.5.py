numbers = list(map(int, input("Введіть числа: ").split()))
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)
