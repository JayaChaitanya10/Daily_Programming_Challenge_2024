def find_missing_number(array, n):
    total_sum = n * (n + 1) // 2
    array_sum = sum(array)
    return total_sum - array_sum

array = [1, 2, 4, 5]
n = 5
print(find_missing_number(array, n))
