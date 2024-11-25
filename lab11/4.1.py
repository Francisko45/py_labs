import random

def file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file]
    return words

def _random(words):
    sample_size = random.randint(1, len(words))
    sample = random.sample(words, sample_size)
    for word in sample:
        print(word)

file_path = 'lab11\index.txt'  

words = file(file_path)
print("Випадкова вибірка слів:")
_random(words)
