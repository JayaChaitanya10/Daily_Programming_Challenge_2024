from collections import defaultdict

def count_k_distinct_substrings(s, k):
    n = len(s)
    start = 0
    count = 0
    char_count = defaultdict(int)

    for end in range(n):
        char_count[s[end]] += 1

        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1

        temp_start = start
        temp_char_count = char_count.copy()

        while len(temp_char_count) == k:
            count += 1
            temp_char_count[s[temp_start]] -= 1
            if temp_char_count[s[temp_start]] == 0:
                del temp_char_count[s[temp_start]]
            temp_start += 1

    return count
