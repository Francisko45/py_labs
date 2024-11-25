ryad = str(input("Введіть рядок: "))
symv = str(input("Введіть символ для пошуку: "))

if len(symv) != 1:
    print("Будь ласка введіть один символ")
else:
    count = 0
    for char in ryad:
        if char == symv:
            count += 1

    print(f"Символ '{symv}' зустрічається у рядку {count} разів")