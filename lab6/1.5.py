synonyms = {}
n = int(input())
for _ in range(n):
    word1, word2 = input().split()
    synonyms[word1] = word2
    synonyms[word2] = word1
find = input()
if find in synonyms:
    print(synonyms[find])
else:
    print("Синонім не знайдено.")
