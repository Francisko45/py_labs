n = int(input())
count = {}

for _ in range(n):
    line = input().split()
    for word in line:
        count[word] = count.get(word, 0) + 1

common = min(count, key=lambda word: (-count[word], word))

print(common)

