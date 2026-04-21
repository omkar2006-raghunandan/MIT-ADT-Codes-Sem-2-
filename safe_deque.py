# Program to implement queue using deque

from collections import deque

queue = deque()

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)

print("Initial Queue:", list(queue))

# Safe dequeue function
def safe_dequeue():
    if len(queue) == 0:
        print("Queue is empty, cannot dequeue.")
        return None
    else:
        return queue.popleft()

# Dequeue elements
print("Dequeued Element:", safe_dequeue())
print("Dequeued Element:", safe_dequeue())
print("Dequeued Element:", safe_dequeue())

# Queue becomes empty now
print("Dequeued Element:", safe_dequeue())