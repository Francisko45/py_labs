import re

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def write_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(item + '\n')

def find_words(text_lines, pattern):
    matched_words = []
    regex = re.compile(pattern)
    for line in text_lines:
        words = line.split()
        for word in words:
            if regex.match(word):
                matched_words.append(word)
    return matched_words

input_file = r'lab11/index.txt'  
output_file = r'lab11/output.txt'
pattern = r'\b\w{5}\b'  

lines = read_file(input_file)
matched_words = find_words(lines, pattern)
write_to_file(output_file, matched_words)

print("Знайдені слова:")
for word in matched_words:
    print(word)
