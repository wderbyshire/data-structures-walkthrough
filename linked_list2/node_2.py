class Node:
    def __init__(self, value=None, pointer: int = None):
        self.value = value
        self.pointer = pointer

    def get_value(self):
        return self.value

    def get_pointer(self) -> int:
        return self.pointer

    def set_value(self, new_value):
        self.value = new_value

    def set_pointer(self, new_pointer: int | None):
        self.pointer = new_pointer

