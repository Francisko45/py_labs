def file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def count_word(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.strip().strip('.,!?"\'').lower() 
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

file_path = 'lab11\index.txt'
text = file(file_path)
word_frequency = count_word(text)
print("Частота слів у файлі:")
print(word_frequency)
