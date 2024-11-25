def reverse(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

_string = input("Input a word: ")
reversed_string = reverse(_string)
print(f"Reversed for {_string} is {reversed_string}")
