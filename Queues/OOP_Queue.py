class Queue:
    def __init__(self, max_queue_size):
        self.queue_array = [None for i in range(max_queue_size)]
        self.front_pointer = 0
        self.back_pointer = 0
        self.current_size = 0

    def is_full(self):
        if self.current_size >= len(self.queue_array):
            return True
        else:
            return False

    def is_empty(self):
        if self.current_size == 0:
            return True
        else:
            return False

    def enqueue(self, new_value):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue_array[self.back_pointer] = new_value
            self.back_pointer += 1
            self.current_size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            temp = self.queue_array[self.front_pointer]
            self.front_pointer += 1
            self.current_size -= 1
            return temp

    def test(self):
        print(self.queue_array)
        print("Front", self.front_pointer)
        print("Back", self.back_pointer)