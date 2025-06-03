

class PrioQueue:
    def __init__(self, max_queue_size):
        self.queue_array = [[None, -1] for i in range(max_queue_size)]
        self.current_size = 0
        self.back_pointer = 0

    def is_full(self):
        if self.current_size == len(self.queue_array):
            return True
        else:
            return False

    def is_empty(self):
        if self.current_size == 0:
            return True
        else:
            return False

    def enqueue(self, new_value, priority=0):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue_array[self.back_pointer] = [new_value, priority]
            self.back_pointer += 1
            self.current_size += 1
            self.bubble_sort()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            temp = self.queue_array[0][0]
            self.queue_array[0] = [None, -1]
            self.current_size -= 1
            self.back_pointer -= 1
            self.bubble_sort()

            return temp

    def bubble_sort(self):
        swap_made = True

        while swap_made:
            swap_made = False
            for i in range(len(self.queue_array) - 1):
                if self.queue_array[i][1] < self.queue_array[i+1][1]:
                    swap_made = True
                    temp = self.queue_array[i]
                    self.queue_array[i] = self.queue_array[i+1]
                    self.queue_array[i + 1] = temp

newPrioQ = PrioQueue(5)
