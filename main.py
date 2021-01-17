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

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def list_len(self):
        if self.head is None:
            print('empty')
            return
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        print(count)

    def insert_list(self, data_list):
        self.head = None
        for items in data_list:
            self.insert_at_end(items)

    def remove_at(self, index):
        if 0 > index >= self.list_len():
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
        if 0 > index >= self.list_len():
            raise Exception('INVALID INDEX')
        if index == 0:
            self.insert_at_beginning(data)
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_duplicate(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head

    def print(self):
        if self.head is None:
            print('list is empty')
            return
        itr = self.head
        lst = ''
        while itr:
            lst += str(itr.data) + '-->'
            itr = itr.next
        print(lst)


ll = linkedList()
ll.insert_list([1, 2, 5, 6, 7])
ll.print()
ll.list_len()
ll.insert_at_beginning(45)
ll.insert_at_beginning(89)
ll.insert_at_end(56)
ll.print()
ll.list_len()
ll.remove_at(2)
ll.print()
ll.list_len()
ll.insert_at(2, 45)
ll.print()
ll.list_len()
ll.remove_duplicate()
ll.print()
ll.list_len()

