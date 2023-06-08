class Queue:
    def __init__(self, max_queue_size: int):
        self.queue_list = [None for i in range(max_queue_size)]
        self.current_size = 0
        self.front_pointer = 0
        self.back_pointer = -1

    def enqueue(self, new_value):
        if not self.is_full():
            self.back_pointer += 1
            self.queue_list[self.back_pointer] = new_value
            self.current_size += 1
        else:
            print("Queue is full")

    def dequeue(self):
        if not self.is_empty():
            temp = self.queue_list[self.front_pointer]
            self.front_pointer += 1
            self.current_size -= 1
        else:
            print("Queue is empty")
            return None

        return temp

    def is_full(self):
        if self.current_size == len(self.queue_list):
            return True
        else:
            return False

    def is_empty(self):
        if self.current_size == 0:
            return True
        else:
            return False

    def print_queue(self):
        print(self.queue_list)
