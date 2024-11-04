text = input("Введіть рядок: ")
first_index = text.find('h')
last_index = text.rfind('h')
modified_text = text[:first_index + 1] + text[first_index + 1:last_index].replace('h', 'H') + text[last_index:]
print(modified_text)
