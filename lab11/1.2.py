def read_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def file(sum, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Сума чисел: {sum}")

input_file = 'lab11\index.txt'
output_file = 'lab11\sum_numbers.txt'
numbers = read_numbers(input_file)
total_sum = sum(numbers)
print(f"Сума чисел: {total_sum}")
file(total_sum, output_file)

