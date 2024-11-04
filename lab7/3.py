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
    integerpart = int(number)
    fractional_part = number - integerpart
    
    binaryinteger = binaryi(integerpart)
    binaryfraction = binaryf(fractional_part)
    
    if binaryfraction:
        return f"{binaryinteger}.{binaryfraction}"
    else:
        return binaryinteger

number = float(input("Введіть десяткове число: "))
res = tobinary(number)
print(f"Двійковий код: {res}")
