one = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine"
}

ten = {
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
}

hundred = {
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}

def reunit(n):
    if n == 1000:
        return "one thousand"
    words = ""
    if n >= 100:
        hundreds = n // 100
        words +=one[hundreds] + " hundred"
        n %= 100
        if n != 0:
            words += " and "
    if 10 <= n < 20:
        words += ten[n]
    else:
        if n >= 20:
            tens_place = (n // 10) * 10
            words += hundred[tens_place]
            n %= 10
            if n != 0:
                words += "-"
        if 1 <= n < 10:
            words += ten[n]
    return words

def countreunit(n):
    words = reunit(n)
    cleaned_words = words.replace(" ", "").replace("-", "")
    return len(cleaned_words)

while True:
    try:
        number = int(input("Введіть ціле число від 1 до <1000:\n"))
        if 1 <= number < 1000:
            words = reunit(number)
            letter_count = countreunit(number)
            print(f"{words}\n{letter_count} букви знадобиться для запису англійською мовою числа {number}")
        else:
            print("Будьте уважні! Введіть ціле число від 1 до <1000:")
    except ValueError:
        print("Будьте уважні! Введіть ціле число від 1 до <1000:")
