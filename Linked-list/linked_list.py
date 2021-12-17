class Node:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        while itr:
            print(str(itr.data), end="-->")
            itr = itr.next
        print()

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)

        else:
            itr = self.head
            while(itr.next != None):
                itr = itr.next
            itr.next = Node(data)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def length(self):
        itr = self.head
        size = 0
        if self.head is not None:
            while itr:
                size += 1
                itr = itr.next

        return size

    def remove_at(self, index):
        if index < 0 or index >= self.length():
            print("Invalid index")

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.length():
            print("Invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data)
                node.next = itr.next
                itr.next = node
                break

            itr = itr.next
            count += 1


if __name__ == "__main__":

    ll = LinkedList()
    """
    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    ll.insert_at_begining(3)
    ll.insert_at_end(100)
    """

    ll.insert_values([1, 2, 3, 4, 5, 111])
    ll.print()
    ll.insert_at(3, 1000)
    ll.print()
