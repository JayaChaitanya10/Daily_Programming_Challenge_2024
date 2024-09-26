def count_divisors(N):
    count = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            count += 1
            if i != N // i:
                count += 1
    return count
