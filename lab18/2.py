import binascii


hex_string = "47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b"


gif = binascii.unhexlify(hex_string)


if gif[:6] == b"GIF89a":
    print("Це правильний GIF-файл")

    width = int.from_bytes(gif[6:8], 'little')
   
    height = int.from_bytes(gif[8:10], 'little')

    print(f"Ширина: {width}")
    print(f"Висота: {height}")
    
    
    if width == 1 and height == 1:
        print("Ширина і висота рівні 1")
    else:
        print("Ширина або висота не рівні 1")
else:
    print("Це не GIF-файл")
