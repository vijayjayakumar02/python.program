from collections import deque


class stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        self.container.pop()

    def size(self):
        return len(self.container)

    def is_empty(self):
        if len(self.container) == 0:
            return 'Empty'
        else:
            return 'Not Empty'

    def print(self):
        print(self.container)


ss = stack()
ss.push(56)
ss.push(85)
ss.pop()
ss.pop()
ss.print()
print(ss.is_empty())