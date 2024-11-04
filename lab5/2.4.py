input = input("Введіть 5 цифр, розділених пробілами: ")
digits = list(map(int, input.split()))
r_digits = digits[::-1]
number = int("".join(map(str, r_digits)))
print("Число зі зворотного списку:", number)
