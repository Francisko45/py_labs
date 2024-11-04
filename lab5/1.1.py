input = "1,2,3,4,5,6,7,8,9"
numbers = input.split(',')
odd = numbers[::2]
data = ",".join(odd)
print(data)
