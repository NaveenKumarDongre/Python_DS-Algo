from node import *

# Creating a linked list

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

# creating a function to traverse a linked list
head = node1
print_llist(head)

"""
print(search_llist(node1, 11))

head = insert_at_begin(node1, 1000)
print_llist(head)

head = inser_at_end(head, 9999)
print_llist(head)

head = insert_at(head, 6, 'a')
print_llist(head)


head = del_last_node(head)
print_llist(head)
"""
# Calling the sorted inserted function

head = sorted_insert(head, 7)
print_llist(head)

head = recurr_reverse1(head)
print_llist(head)
