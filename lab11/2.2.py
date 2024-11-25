import os
def copy_file(source, destination):
    with open(source, 'r', encoding='utf-8') as src:
        data = src.read()
    
    with open(destination, 'w', encoding='utf-8') as dest:
        dest.write(data)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


source_file = 'lab11\source.txt'
destination_file = 'lab11\destination.txt'
    
    
copy_file(source_file, destination_file)
copied_data = read_file(destination_file)
print("Скопійовані дані:")
print(copied_data)
os.remove(source_file)
print(f"Файл {source_file} було видалено.")

