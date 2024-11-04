a =input ().split()
while len(a) > 1:
    max_value = max(a)
    a.remove(max_value)
print(a)