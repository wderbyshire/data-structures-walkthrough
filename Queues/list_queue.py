class ListQueue:
    def __init__(self):
        self.queue_list = []

    def enqueue(self, new_value):
        self.queue_list.append(new_value)

    def dequeue(self):
        if self.queue_list:
            return self.queue_list.pop(0)
        else:
            return "Queue is empty"
