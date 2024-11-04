def binaryi(n):
    result = ''
    q = n
    while q != 0:
        r = q % 2
        result = str(r) + result
        q //= 2
    return result if result else '0'
def binaryf(fraction, precision=10):
    result = ''
    q = fraction
    while precision > 0:
        q *= 2
        bit = int(q)
        result += str(bit)
        q -= bit
        precision -= 1
    return result

def tobinary(number):
    integer_part = int(number)
    fractional_part = number - integer_part
    
    binary_integer = binaryi(integer_part)
    binary_fraction = binaryf(fractional_part)
    
    if binary_fraction:
        return f"{binary_integer}.{binary_fraction}"
    else:
        return binary_integer

number = float(input("Введіть десяткове число: "))
binary_representation = tobinary(number)
print(f"Двійковий код: {binary_representation}")
