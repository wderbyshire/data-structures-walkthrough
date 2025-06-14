class Stack:
    def __init__(self, max_stack_size: int):
        self.stack_array = [None for i in range(max_stack_size)]
        self.front_pointer = -1

    def is_full(self):
        if self.front_pointer + 1 == len(self.stack_array):
            return True
        else:
            return False

    def is_empty(self):
        if self.front_pointer == -1:
            return True
        else:
            return False

    def stack_push(self, new_value):
        if not self.is_full():
            self.front_pointer += 1
            self.stack_array[self.front_pointer] = new_value
        else:
            print("Stack is full")

    def stack_pop(self):
        if not self.is_empty():
            temp = self.stack_array[self.front_pointer]
            self.front_pointer -= 1
            return temp
        else:
            print("Stack is empty")














