def file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def words(text):
    words = text.lower().split()
    unique_words = set(words)
    return list(unique_words)

file_path = 'lab11\index.txt'

text = file(file_path)
unique_words = words(text)
print("Список унікальних слів:")
for word in unique_words:
    print(word)
