n = int(input("Введіть значення n: "))
sum = 1  
for i in range(2, n + 1):
    if i % 2 == 0:
        sum += i
    else:
        sum -= i

print(f"Summ 1 + 2 − 3 + 4 − 5 + ... ±n where n = {n} is {sum}")
