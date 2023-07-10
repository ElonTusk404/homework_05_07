def sum_digits(num: int):
    if not isinstance(num, int):
        raise TypeError('Argument must be only integer')
    if num == 0:
        return num
    
    return num % 10 + sum_digits(num // 10)
print(sum_digits('omg'))