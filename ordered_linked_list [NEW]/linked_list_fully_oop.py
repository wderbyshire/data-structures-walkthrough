from node_fully_oop import OopNode

"""A fully OOP version of a linked list, where nodes are objects that are logically linked to each other. Linked list 
class only contains the rules and the starting node"""

class OopOrderedLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, new_value):
        new_node = OopNode(new_value)

        if self.head is None:
            self.head = new_node
        elif new_node.value < self.head.value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and new_node.value > current.next_node.value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def delete_node(self, value_to_delete):
        if self.head is None:
            print("List is empty, you can't delete node")
            return

        current_node = self.head

        if current_node.value == value_to_delete:
            self.head = current_node.next_node
        else:
            while current_node.next_node is not None and current_node.next_node.value != value_to_delete:
                current_node = current_node.next_node

            if current_node.next_node is None:
                print("Node doesn't exist in list")
            else:
                current_node.next_node = current_node.next_node.next_node

    def traverse_logically(self):
        if self.head is None:
            print("No nodes to print")
            return

        current_node = self.head
        print(self.head.value)

        while current_node.next_node is not None:
            current_node = current_node.next_node
            print(current_node.value)

new_ll = OopOrderedLinkedList()
new_ll.delete_node("Ana")
new_ll.add_node("Nancy")
new_ll.add_node("Ava")
new_ll.add_node("Dave")
new_ll.add_node("Eva")
new_ll.add_node("Peter")
new_ll.add_node("Rose")
new_ll.add_node("Ana")
new_ll.delete_node("Ana")
new_ll.traverse_logically()