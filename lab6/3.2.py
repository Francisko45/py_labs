a = [1, 2, 3, 3, 4, 4, 5, 6, 7, 7,]
b = set()
for number in a:
    if number in b:
        print("YES")
    else:
        print("NO")
        b.add(number)
