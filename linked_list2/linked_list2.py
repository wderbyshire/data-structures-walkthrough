from node_2 import Node


class LinkedList:
    def __init__(self, size: int):
        self.nodes_list = []

        self.start = None
        self.next_free = 0

        for i in range(size):
            new_node = Node(pointer=i+1)
            self.nodes_list.append(new_node)

            if i == size-1:
                new_node.set_pointer(None)


