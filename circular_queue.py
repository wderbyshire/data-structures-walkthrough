import queues


class CircularQueue(queues.Queue):
    def __init__(self, max_queue_size):
        super().__init__(max_queue_size)

    def enqueue(self, new_value):
        if not self.is_full():
            self.back_pointer += 1
            self.back_pointer %= len(self.queue_list)
            self.queue_list[self.back_pointer] = new_value
            self.current_size += 1
        else:
            print("Queue is full")

    def dequeue(self):
        if not self.is_empty():
            temp = self.queue_list[self.front_pointer]
            self.front_pointer += 1
            self.front_pointer %= len(self.queue_list)
            self.current_size -= 1
        else:
            print("Queue is empty")
