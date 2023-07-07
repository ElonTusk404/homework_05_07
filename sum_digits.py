def sum_digits(num: int):
    if num == 0:
        return num
    
    return num % 10 + sum_digits(num // 10)
print(sum_digits(155))