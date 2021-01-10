class binary_tree_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = binary_tree_node(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binary_tree_node(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements


def build_tree(elements):
    root = binary_tree_node(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    number_tree = build_tree(numbers)
    print(number_tree.in_order_traversal())
