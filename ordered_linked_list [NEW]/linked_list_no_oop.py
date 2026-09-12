

def add_node_to_ll(ll_to_add, value_to_add, head, next_free):
    if next_free is None:
        print("List is full, cannot add another item")
        return head, next_free

    new_node = ll_to_add[next_free]
    new_node[0] = value_to_add

    if head is None or new_node[0] < ll_to_add[head][0]:
        temp = next_free
        next_free = new_node[1]
        new_node[1] = head
        head = temp
    else:
        current_node = ll_to_add[head]

        while current_node[1] is not None and new_node[0] > ll_to_add[current_node[1]][0]:
            current_node = ll_to_add[current_node[1]]

        temp = next_free
        next_free = new_node[1]
        new_node[1] = current_node[1]
        current_node[1] = temp

    return head, next_free

def delete_node_from_ll(ll_to_delete_from, value_to_delete, head,  next_free):
    if head is None:
        print("List is empty, you can't delete node")
        return head, next_free

    current_node = ll_to_delete_from[head]

    if current_node[0] == value_to_delete:
        temp = next_free
        next_free = head
        head = current_node[1]
        current_node[1] = temp
    else:
        while current_node[1] is not None and value_to_delete != ll_to_delete_from[current_node[1]][0]:
            current_node = ll_to_delete_from[current_node[1]]

        if current_node[1] is None:
            print("Node to delete not found")
            return head, next_free
        else:
            node_to_delete = ll_to_delete_from[current_node[1]]
            temp = next_free
            next_free = current_node[1]
            current_node[1] = node_to_delete[1]
            node_to_delete[1] = temp

    return head, next_free

def traverse_ll_logically(ll, head):
    current_node = ll[head]
    print(current_node[0])
    while current_node[1] is not None:
        current_node = ll[current_node[1]]
        print(current_node[0])

def test():
    linked_list = [[None, i+1] for i in range(6)]
    linked_list[len(linked_list) - 1][1] = None
    ll_head = None
    ll_next_free = 0

    ll_head, ll_next_free = add_node_to_ll(linked_list,  "Nancy", ll_head,  ll_next_free)
    ll_head, ll_next_free = add_node_to_ll(linked_list,  "Ava", ll_head,  ll_next_free)
    ll_head, ll_next_free = add_node_to_ll(linked_list,  "Dave", ll_head,  ll_next_free)
    ll_head, ll_next_free = add_node_to_ll(linked_list,  "Peter", ll_head,  ll_next_free)
    ll_head, ll_next_free = add_node_to_ll(linked_list,  "Rose", ll_head,  ll_next_free)
    ll_head, ll_next_free = add_node_to_ll(linked_list,  "Ana", ll_head,  ll_next_free)
    ll_head, ll_next_free = add_node_to_ll(linked_list,  "Mario", ll_head,  ll_next_free)

    ll_head, ll_next_free = delete_node_from_ll(linked_list, "Nancy", ll_head, ll_next_free)
    ll_head, ll_next_free = delete_node_from_ll(linked_list, "Ana", ll_head, ll_next_free)
    ll_head, ll_next_free = add_node_to_ll(linked_list,  "Mario", ll_head,  ll_next_free)

    traverse_ll_logically(linked_list, ll_head)

test()