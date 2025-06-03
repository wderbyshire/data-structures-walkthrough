from linked_list import LinkedList


if __name__ == "__main__":
    new_linked_list = LinkedList(5)

    new_linked_list.add_node("Nancy")

    new_linked_list.add_node("Ava")

    new_linked_list.add_node("Dave")

    new_linked_list.add_node("Peter")

    # new_linked_list.delete_node_by_value("Dave")

    new_linked_list.add_node("Peter")

    print(new_linked_list)
