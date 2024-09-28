def sort_stack(stack):
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        insert_sorted(stack, temp)

def insert_sorted(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
    else:
        temp = stack.pop()
        insert_sorted(stack, element)
        stack.append(temp)

# Example usage:
stack = [3, -2, 5, 1, 0]
sort_stack(stack)
print(stack)
