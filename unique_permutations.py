from itertools import permutations

def unique_permutations(s):
    return list(set(''.join(p) for p in permutations(s)))

# Example usage
s = "abc"
print(unique_permutations(s))
