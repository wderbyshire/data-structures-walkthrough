input_list = [17, 8, 4, 12, 22, 19, 14, 5, 30, 25]
bst_array = [[]] * 10
next_free = 0


def add_node(value):
    global bst_array, next_free

    bst_array[next_free] = [None, value, None]

    next_free += 1

    if next_free == 1:
        return
    else:
        current_node = 0
        while True:
            if value < bst_array[current_node][1]:
                if bst_array[current_node][0] is None:
                    bst_array[current_node][0] = next_free - 1
                    break
                else:
                    current_node = bst_array[current_node][0]
            elif value > bst_array[current_node][1]:
                if bst_array[current_node][2] is None:
                    bst_array[current_node][2] = next_free - 1
                    break
                else:
                    current_node = bst_array[current_node][2]

def print_bst():
    for node in bst_array:
        print(node)

def search_bst(search_term):
    current_node = 0

    while True:
        if search_term == bst_array[current_node][1]:
            return True
        elif search_term < bst_array[current_node][1]:
            if bst_array[current_node][0] is None:
                return False
            else:
                current_node = bst_array[current_node][0]
        elif search_term >  bst_array[current_node][1]:
            if  bst_array[current_node][2] is None:
                return False
            else:
                current_node = bst_array[current_node][2]

for new_value in input_list:
    add_node(new_value)

print_bst()

print(search_bst(17))
print(search_bst(25))
print(search_bst(5))
print(search_bst(12))
print(search_bst(22))
print(search_bst(45))
print(search_bst(1))