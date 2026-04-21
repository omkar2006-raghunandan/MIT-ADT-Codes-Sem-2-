# Program to implement stack using list

stack = []

# Push elements into stack
stack.append(10)
stack.append(20)
stack.append(30)

print("Initial Stack:", stack)

# Safe pop function
def safe_pop():
    if len(stack) == 0:
        print("Stack is empty, nothing to pop.")
        return None
    else:
        return stack.pop()

# Pop elements
print("Popped Element:", safe_pop())
print("Popped Element:", safe_pop())
print("Popped Element:", safe_pop())

# Stack becomes empty now
print("Popped Element:", safe_pop())