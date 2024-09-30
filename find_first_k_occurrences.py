def find_first_k_occurrences(arr, k):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    for num in arr:
        if count[num] == k:
            return num
    return -1
