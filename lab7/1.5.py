a = input("Vvedite cherez probel: ").split()
num = list(map(int, a[0::2]))  
step = list(map(int, a[1::2]))  
def res(num, step):
    result = []
    for n, s in zip(num, step):
        result.append(n ** s)  
    return result
print(res(num, step))
