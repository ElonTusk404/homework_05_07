def binary_search_recursive(array, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if array[mid] == target:
        return mid
    
    
    if array[mid] > target:
        return binary_search_recursive(array, target, low, mid - 1)
    else:
        return binary_search_recursive(array, target, mid + 1, high)
