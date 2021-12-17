class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# creating a function to traverse a linked list


def print_llist(head):
    itr = head
    while itr:
        print((itr.data), end="-->")
        itr = itr.next
    print()

# Search in a linked-list and returning the index
# If not found return -1


def search_llist(head, key):
    itr = head

    i = 0
    while itr:
        if itr.data == key:
            return i
        i = i + 1
        itr = itr.next
    return -1

# Inserting at the begining of the linked list and
# returning the new head


def insert_at_begin(head, data):
    new_node = Node(data)
    if head == None:
        return new_node
    else:
        new_node.next = head
        return new_node

# Inserting at the end of the linked list


def inser_at_end(head, data):
    new_node = Node(data)
    if head == None:
        return new_node
    itr = head
    while itr.next:
        itr = itr.next
    itr.next = new_node
    return head


# Inserting node at a particular position


def insert_at(head, pos, data):
    new_node = Node(data)
    if pos <= 0 or head == None:
        return head

    elif pos == 1:
        new_node.next = head
        return new_node

    itr = head
    for _ in range(pos-2):
        itr = itr.next
        if itr == None:
            return head
    new_node.next = itr.next
    itr.next = new_node

    return head


# Deleting last Node of the linked list

def del_last_node(head):
    if head == None or head.next == None:
        return None
    itr = head

    while itr.next.next:

        itr = itr.next

    itr.next = None
    return head

# Sorted insert in a linked list


def sorted_insert(head, data):
    new_node = Node(data)

    if head == None or head.data > new_node.data:
        new_node.next = head
        return new_node

    itr = head
    while(itr.next != None and itr.next.data < data):
        itr = itr.next

    new_node.next = itr.next
    itr.next = new_node

    return head

# reverse a linked list


def reverse_list(head):
    curr = head
    prev = None
    while curr:
        next_p = curr.next
        curr.next = prev
        prev = curr
        curr = next_p

    return prev


def recurr_reverse1(head):

    if head == None:
        return head

    if head.next == None:
        return head

    rest_head = recurr_reverse1(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None
    return rest_head
