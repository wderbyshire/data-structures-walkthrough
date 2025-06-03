from . import LinkedListNode


class LinkedList:
    def __init__(self, size: int):
        self.node_collection = []

        for i in range(size):
            if i != size-1:
                new_node = LinkedListNode(pointer=i+1)
            else:
                new_node = LinkedListNode()

            self.node_collection.append(new_node)

        self.start = None
        self.next_free = 0

    def node_peek(self, node_index) -> int:
        return self.node_collection[node_index].pointer

    def return_list(self) -> list[LinkedListNode]:
        temp_list = []

        current_node_index = self.start

        while current_node_index is not None:
            temp_list.append(self.node_collection[current_node_index])

            current_node_index = self.node_peek(current_node_index)

        return temp_list

    def add_node(self, new_value) -> None:
        if self.next_free is None:
            # If the next_free pointer is pointing at nothing, the list is full and can't be added to
            print("Error adding new node: Linked list is full")

            # Escape the function
            return
        elif self.start is None:
            # If the start pointer is pointing to None, then it means the linked list is empty, meaning that we should
            #  insert our new node to the "start" of the linked list

            new_node = self.node_collection[self.next_free]
            new_node.set_value(new_value)

            # Because this is the first node, it is automatically the largest, and therefore points at nothing
            new_node.set_pointer(None)

            # Because this is the first node, it is automatically the smallest, and therefore the start must point to it
            self.start = 0

            self.find_next_free()

            # Break out of the function
            return

        # The insertion sort starts at the start index
        current_node_index = self.start

        # We keep track of the previously checked node. It initialises to None
        previous_node = None

        # We "create" a new node at the index indicated by the self.next_free pointer and insert our new value
        new_node = self.node_collection[self.next_free]
        new_node.set_value(new_value)

        # Loop through the linked list in order
        while current_node_index is not None:
            # Set the currently working node to the pointer of the previous node
            current_node = self.node_collection[current_node_index]

            if new_value <= current_node.get_value():
                # If the value of the new node is less than or equal to the current node, we set the new nodes pointer
                #  to the current pointer
                new_node.set_pointer(current_node_index)

                if previous_node is None:
                    # If there was no previous node, it means that the new node should be to the "front" of the linked
                    #  list, meaning that no nodes need to change their pointer, but the start pointer needs to change
                    #  to be the index of the new node (which is indicated by the next_free pointer)
                    self.start = self.next_free
                else:
                    # If there was a previous node, the previous node needs to point to the new node's index
                    previous_node.set_pointer(self.next_free)

                # Find the next free index
                self.find_next_free()

                # Break out of the loop
                break
            elif new_value > current_node.get_value():
                # If the new_value is greater than the current node, we continue the loop and set the previous node to
                #  be the current node
                previous_node = current_node

            # To continue the loop, we find the index of the next node by peeking
            current_node_index = self.node_peek(current_node_index)

            if current_node_index is None:
                # If the current node was pointing at None, then we've arrived at the "end" of the linked list. This
                #  means that the new_node is the largest value in the list. We set the current_nodes pointer to be
                #  the index of the new node, indicated by the next_free pointer
                current_node.set_pointer(self.next_free)

                # Because the current node is the largest, it's pointer should be set to None
                new_node.set_pointer(None)

                # Find the next free index
                self.find_next_free()

    def delete_node_by_value(self, value_to_delete):
        if self.start is None:
            # If the start pointer points at nothing, the list has no nodes, and cannot perform a delete
            print("The linked list is empty, cannot delete a node")
            return

        # Track the node to be deleted along with its index and initialise it to None
        node_to_delete = None
        index_of_node_to_delete = None

        # Search for a node with the value passed into the method, if found, set the previous trackers to their
        #  appropriate value
        for index, node in enumerate(self.node_collection):
            if node.value == value_to_delete:
                node_to_delete = node
                index_of_node_to_delete = index
                break

        # If the previous loop didn't find a node with the value passed into the method, that node doesn't exist. Escape
        #  out of the method and print an error message
        if node_to_delete is None:
            print(f"No node with the value '{value_to_delete}' exists in this linked list")
            return

        # If a node was found, we can now delete it
        if self.start == index_of_node_to_delete:
            # If the node is at the "start" of the list, the only thing that needs to change is the start pointer, which
            #  should now point at whatever the deleted node was pointing at
            self.start = node_to_delete.get_pointer()
        else:
            # If the node is not the start, then we need to find the previous node that was pointing at the node to be
            #  deleted
            for node in self.node_collection:
                if node.get_pointer() == index_of_node_to_delete:
                    # Once the previous node is found, we set that node to now point at what the deleted node was
                    #  pointing at and escape the loop
                    node.set_pointer(node_to_delete.get_pointer())
                    break

        # In order for this node to be registered as an "empty" node to be seen by the next_free pointer, we set its
        #  value to be None
        node_to_delete.set_value(None)

        # Run the find next free pointer method, which can now be the recently deleted nodes index
        self.find_next_free()

    def find_next_free(self) -> None:
        # The next free pointer starts as None
        self.next_free = None

        # Loop through the node_collection until an "empty" node is found
        for i in range(len(self.node_collection)):
            if self.node_collection[i].value is None:
                # When an empty node is found, the next free pointer is set to the current index
                self.next_free = i

                # The loop is escaped
                break

        # If the for loop managed to cycle through the whole list without being escaped, the next_free pointer will be
        #  pointing at None, meaning the linked list is full

    def __str__(self):
        return str([i.get_value() for i in self.return_list()])

    def __repr__(self):
        return str([f"Value: {node.get_value()}, Pointing at: {node.get_pointer()}"
                    for index, node in enumerate(self.return_list())])
