new_queue = [None, None, None, None]
front_pointer = 0
back_pointer = 0
current_size = 0

def is_full():
    if current_size >= len(new_queue):
        return True
    else:
        return False

def is_empty():
    if current_size == 0:
        return True
    else:
        return False

def enqueue(new_value):
    global front_pointer, current_size
    if is_full():
        print("The queue is full")
    else:
        new_queue[front_pointer] = new_value
        front_pointer += 1
        current_size += 1

def dequeue():
    global back_pointer, current_size
    if is_empty():
        print("The queue is empty")
    else:
        print(new_queue[back_pointer])
        back_pointer += 1
        current_size -=1


enqueue("Word")
enqueue("Song")
dequeue()
enqueue("Poem")
