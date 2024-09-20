def is_valid(s):
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket:
            if not stack or stack.pop() != matching_bracket[char]:
                return False
    return not stack

# Example usage
s = "()[]{}"
print(is_valid(s))
