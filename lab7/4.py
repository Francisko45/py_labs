def sentencechar(sentence):
    return [char for char in sentence if char != ' ']

def countchar(char_list):
    char_count = {}
    for char in char_list:
        if char in char_count:
            char_count[char] += 1 
        else:
            char_count[char] = 1  
    return char_count

def main():
    sentence = input("Введіть речення: ")
    
    char_list = sentencechar(sentence)
    
    char_count = countchar(char_list)
    
    print("Кількість символів у реченні:", char_count)

if __name__ == "__main__":
    main()
