def Sorting(arr, n):
    start = 0
    mid = 0
    end = n - 1
    
    while mid <= end:
        if arr[mid] == 0:
            arr[mid], arr[start] = arr[start], arr[mid]
            start += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[end] = arr[end], arr[mid]
            end -= 1

n = int(input())
arr = list(map(int, input().split()))
Sorting(arr, n)
print(arr)