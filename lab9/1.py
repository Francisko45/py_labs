def calculate(first_num, second_num, operation):
    try:
        if operation == '+':
            result = first_num + second_num
        elif operation == '-':
            result = first_num - second_num
        elif operation == '*':
            result = first_num * second_num
        elif operation == '/':
            result = first_num / second_num
        elif operation == 'mod':
            result = first_num % second_num
        elif operation == 'pow':
            result = first_num ** second_num
        elif operation == 'div':
            result = first_num // second_num
        else:
            return "Unsupported operation"
    except ZeroDivisionError:
        return "Division by zero!"
    else:
        return result
    finally:
        print("Calculation attempted")

first_num = float(input("Введіть перше число: "))
second_num = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, /, *, mod, pow, div): ")

result = calculate(first_num, second_num, operation)
print(f"Результат: {result}")
