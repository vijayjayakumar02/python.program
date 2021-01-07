class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.head
        lst = ''
        while itr:
            lst += str(itr.data) + '-->'
            itr = itr.next
        print(lst)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        if 0 > index >= self.get_length():
            raise Exception('INVALID INDEX')
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if 0 > index >= self.get_length():
            raise Exception('INVALID INDEX')
        if index == 0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


ll = linkedList()
ll.insert_at_beginning(56)
ll.insert_at_beginning(89)
ll.insert_at_end(96)
ll.remove_at(0)
ll.insert_at(0, 2)
ll.print()