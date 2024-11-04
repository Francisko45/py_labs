import random
array = [random.randint(-10, 10) for _ in range(21)]
print("Згенерований масив:", array)
positive = [num for num in array if num > 0]
if len(positive) >= 6:
    product = positive[1] * positive[3] * positive[5]
    print("Добуток 2-го, 4-го і 6-го додатного елемента:", product)
else:
    print("У масиві недостатньо додатних елементів.")
