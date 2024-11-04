a = {1, 3, 4, 5, 6, 5, 1, 9}
count = len (a)
evencount = sum(1 for num in a if num != a)
print(f" {evencount}")