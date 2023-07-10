class TargetNotFoundException(Exception):
    pass

def binary_search_recursive(array, target, low, high):
    if low > high:
        raise TargetNotFoundException("Target not found in the list")
    if not isinstance(array, list):
        raise TypeError('Only list')
    if low > high:
        return -1
    mid = (low + high) // 2
    if array[mid] == target:
        return mid
    
    
    if array[mid] > target:
        return binary_search_recursive(array, target, low, mid - 1)
    else:
        return binary_search_recursive(array, target, mid + 1, high)
