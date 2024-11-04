numbers = list(map(int, input("Введіть список чисел, розділених пробілами: ").split()))
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
print("Список після обміну:", numbers)
