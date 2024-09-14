def find_zero_sum_subarrays(array):
    sum_dict = {}
    current_sum = 0
    result = []

    for i in range(len(array)):
        current_sum += arr[i]
        
        if current_sum == 0:
            result.append((0, i))
        
        if current_sum in sum_dict:
            for start in sum_dict[current_sum]:
                result.append((start + 1, i))
        
        if current_sum in sum_dict:
            sum_dict[current_sum].append(i)
        else:
            sum_dict[current_sum] = [i]

    return result

array = [1, 2, -3, 3, -1, 2]
print(find_zero_sum_subarrays(array))
