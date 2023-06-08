"""
A scripted way to implement a queue. Contains all the relevant methods for a queue: enqueue, dequeue, check_empty,
check_full, check_size
"""

new_queue = [None, None, None, None, None, None]

front_pointer = 0
back_pointer = -1
current_size = 0

# Add an item to a queue (enqueue)
new_value = "John Benson"
back_pointer += 1
new_queue[back_pointer] = new_value
current_size += 1

# Enqueue
new_value = "Ben Johnson"
back_pointer += 1
new_queue[back_pointer] = new_value
current_size += 1

# Read item from the front of the queue (dequeue)
dequeued_item = new_queue[front_pointer]
front_pointer += 1
current_size -= 1

# Check if queue is empty
if current_size == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")

# Check if queue is full
if current_size == len(new_queue):
    print("Queue is full")
else:
    print("Queue is not full")

