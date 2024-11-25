def find_max(numbers):
    if not numbers: 
        return None  
    max_value = numbers[0]
     
    for num in numbers:
        if num > max_value:
            max_value = num
    
    return max_value
nums = [3, 7, -2, 10, 5]
result = find_max(nums)
print(f"Максимальне значення: {result}")
