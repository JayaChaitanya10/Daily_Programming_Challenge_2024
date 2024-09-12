def merge(array1, array2, m, n):
    i = m - 1
    j = 0

    while i >= 0 and j < n:
        if array1[i] > array2[j]:
            array1[i], array2[j] = array2[j], array1[i]
        i -= 1
        j += 1

    array1.sort()
    array2.sort()

m = int(input("Enter the size of array1: "))
array1 = list(map(int, input(f"Enter {m} sorted elements for array1: ").split()))

n = int(input("Enter the size of array2: "))
array2 = list(map(int, input(f"Enter {n} sorted elements for array2: ").split()))

merge(array1, array2, m, n)

print("Merged array1:", array1)
print("Merged array2:", array2)
