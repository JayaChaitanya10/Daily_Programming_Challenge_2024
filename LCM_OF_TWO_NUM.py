import math
n, m = map(int, input().split())
lcm = (n * m) // math.gcd(n, m)
print(lcm)
