class Node:
    def __init__(self, value):
        self.right: Node | None = None
        self.value = value
        self.left: Node | None = None


class BinTree:
    def __init__(self):
        self.root: Node | None = None

    def add_node(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return
        else:
            current_node = self.root

        while True:
            if new_node.value < current_node.value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
            else:
                break

    def search_value(self, value):

        if self.root is None:
            return False
        else:
            current_node = self.root

        while True:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    return False
            elif value > current_node.value:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    return False

    def in_order(self, node: Node):
        if node.left is not None:
            self.in_order(node.left)

        print(node.value, end=", ")

        if node.right is not None:
            self.in_order(node.right)


    def pre_order(self, node: Node):
        pass

    def post_order(self, node: Node):
        pass

