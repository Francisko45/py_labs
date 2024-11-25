def to_fiel(strings, filename): 
    file = open(filename, 'w', encoding='utf-8')
    for string in strings:
        file.write(string + '\n')
   
    file.close()

lines = ["pens", "coocked", "gouda", "dobrogo vechora mi z ukraini"]
to_fiel(lines, "output.txt")
