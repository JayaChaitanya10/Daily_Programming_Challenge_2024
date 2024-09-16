def reverse_words(s: str) -> str:
    words = s.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    return result

s = "  Hello   world!  How are  you?   "
print(reverse_words(s))
