db = {}
def factorial(number: int):
    try:
        if number == 0 or number == 1:
            return 1
        if number in db:
            return db[number]
        
        result = number * factorial(number - 1)
        db[number] = result
    except TypeError:
        raise TypeError('Agrument must be integer.')
    except RecursionError:
        raise RecursionError('Recursion limits reached.')
    return result
