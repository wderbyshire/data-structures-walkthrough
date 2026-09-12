from node import Node


class OrderedLinkedList:
    def __init__(self, starting_size):
        self.head = None
        self.next_free = 0
        self.node_array = [None for i in range(starting_size)]

        # Populate array with empty nodes
        for i in range(len(self.node_array)):
            if i == starting_size - 1:
                # If node is the final node in the array, set pointer to None
                new_node = Node(None)
            else:
                new_node = Node(i+1)

            self.node_array[i] = new_node

    def add_node(self, new_value):
        # If linked list is full, prevent node from being added
        if self.next_free is None:
            print("List is full, cannot add another item")
            return

        # If linked list has space, add new value to next free node
        new_node = self.node_array[self.next_free]

        new_node.value = new_value

        # If the list is empty...
        if self.head is None or new_node.value < self.node_array[self.head].value:
            temp = self.next_free
            self.next_free = new_node.next_pointer
            new_node.next_pointer = self.head
            self.head = temp
        else:
            # Traverse linked list to find position of insertion

            # Start at the head node
            current_node = self.node_array[self.head]

            # Loop through logical order of linked list, comparing the new value with the value of the next node. This
            #  way, the current node will always be the previous node checked.
            while (current_node.next_pointer is not None and
                   new_node.value > self.node_array[current_node.next_pointer].value):
                # Move onto the next node
                current_node = self.node_array[current_node.next_pointer]

            # Once an insertion point is found, update all the pointers
            temp = self.next_free
            self.next_free = new_node.next_pointer
            new_node.next_pointer = current_node.next_pointer
            current_node.next_pointer = temp

    def delete_node(self, value_to_delete):
        # Check that list contains nodes
        if self.head is None:
            print("List is empty, you can't delete node")
            return

        current_node = self.node_array[self.head]

        # Check to see if node to delete is at the head
        if current_node.value == value_to_delete:
            temp = self.next_free
            self.next_free = self.head
            self.head = current_node.next_pointer
            current_node.next_pointer = temp
        else:
            # Loop through logical order and compare value to delete with value in the next node. This way, the current
            #  node will always be the previous node checked
            while (current_node.next_pointer is not None and
                   value_to_delete != self.node_array[current_node.next_pointer].value):
                current_node = self.node_array[current_node.next_pointer]

            # If the current node's pointer is None, then we've traversed the full list and not found the value to
            #  delete
            if current_node.next_pointer is None:
                print("Node to delete not found")
            else:
                node_to_delete = self.node_array[current_node.next_pointer]
                temp = self.next_free
                self.next_free = current_node.next_pointer
                current_node.next_pointer = node_to_delete.next_pointer
                node_to_delete.next_pointer = temp

    def print_chronological(self):
        print("Head:", self.head)
        print("Next free:", self.next_free)
        for index, node in enumerate(self.node_array):
            print(index, node.value, node.next_pointer)
        print()

    def print_logical(self):
        if self.head is None:
            print("No nodes to print")
            return

        current_node = self.node_array[self.head]
        print(current_node.value)

        while current_node.next_pointer is not None:
            current_node = self.node_array[current_node.next_pointer]
            print(current_node.value)


new_ll = OrderedLinkedList(6)
new_ll.add_node("Nancy")
new_ll.add_node("Ava")
new_ll.add_node("Dave")
new_ll.add_node("Ana")
new_ll.add_node("Rose")


new_ll.delete_node("Peter")
new_ll.add_node("Mario")
new_ll.print_logical()
new_ll.print_chronological()
# new_ll.delete_node("Ana")
# new_ll.print_logical()