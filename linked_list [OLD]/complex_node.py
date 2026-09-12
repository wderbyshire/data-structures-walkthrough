class ComplexLinkedListNode:
    def __init__(self, value=None, pointer: int | None = None):
        self.value = value
        self.pointer = pointer

    def get_value(self):
        return self.value

    def set_value(self, new_value) -> None:
        self.value = new_value

    def get_pointer(self) -> int:
        return self.pointer

    def set_pointer(self, new_pointer: int) -> None:
        self.pointer = new_pointer

    def _is_valid_operand(self, other):
        return self.__class__ == other.__class__

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return self.value == other.value

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return self.value < other.value

    def __le__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return self.value <= other.value

    def __gt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return self.value > other.value

    def __ge__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return self.value >= other.value
