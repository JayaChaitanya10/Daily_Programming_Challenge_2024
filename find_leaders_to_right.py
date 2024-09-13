def find_leaders(array, n):
    leaders = []
    max_from_right = array[-1]
    leaders.append(max_from_right)
    
    for i in range(n - 2, -1, -1):
        if array[i] > max_from_right:
            max_from_right = array[i]
            leaders.append(max_from_right)
    
    return leaders[::-1]

array = [16, 17, 4, 3, 5, 2]
n = len(array)
print(find_leaders(array, n))
