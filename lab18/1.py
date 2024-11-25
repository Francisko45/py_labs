import re


text = input("Введіть текст для пошуку: ")


print("Слова, що починаються з 'c':", re.findall(r'\bc\w*', text))


print("Чотирилітерні слова, що починаються з 'c':", re.findall(r'\bc\w{3}\b', text))


print("Слова, що закінчуються на 'r':", re.findall(r'\b\w*r\b', text))


print("Слова, що містять 'time':", re.findall(r'\b\w*time\w*\b', text))
