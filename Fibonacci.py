def fibonacci(number: int):
    try:
        if number <=2 :
            return 1
        return fibonacci(number - 1) +  fibonacci(number - 2)
    except TypeError:
        raise TypeError('Number argument must be integer.')
