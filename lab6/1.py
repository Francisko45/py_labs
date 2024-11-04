def count(input):
    char_count = {}
    
    for char in input:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count

input = "Lorem ipsum dolor sit amet"
result = count(input)
print(result)