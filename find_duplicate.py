def findDuplicate(array):
    low = 1
    high = len(array) - 1
    
    while low < high:
        mid = (low + high) // 2
        count = sum(1 for num in array if num <= mid)
        
        if count > mid:
            high = mid
        else:
            low = mid + 1
    
    return low
