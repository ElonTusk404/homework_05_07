class TargetNotFoundException(Exception):
    pass
def binary_search(nums, target):
    if not isinstance(nums, list):
        raise TypeError('Only list')
    try:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
    except Exception:
        raise TargetNotFoundException('Target not found in the list')
    return -1
    
