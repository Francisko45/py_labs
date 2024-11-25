num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

print("Виберіть дію:")
print("1 - Сума трьох чисел")
print("2 - Добуток трьох чисел")
vyb = int(input("Ваш вибір: "))

if vyb == 1:
    res = num1 + num2 + num3
    print(f"Сума чисел: {res}")
elif vyb == 2:
    res = num1 * num2 * num3
    print(f"Добуток чисел: {res}")

