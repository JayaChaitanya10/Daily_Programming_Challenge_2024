def reverse_stack(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(top)
