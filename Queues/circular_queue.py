from OOP_Queue import Queue


class CircularQueue(Queue):
    def __init__(self, max_queue_size):
        super().__init__(max_queue_size)

    def enqueue(self, new_value):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue_array[self.back_pointer] = new_value
            self.back_pointer += 1
            self.current_size += 1
            if self.back_pointer >= len(self.queue_array):
                self.back_pointer = 0

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            temp = self.queue_array[self.front_pointer]
            self.front_pointer += 1
            self.current_size -= 1
            if self.front_pointer >= len(self.queue_array):
                self.front_pointer = 0
            return temp
