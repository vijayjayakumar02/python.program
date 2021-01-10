class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print()


def build_product_tree():
    ceo = TreeNode('VARSHA (CEO)')

    infra_head = TreeNode('MELVIN (Infrastructure head)')
    infra_head.add_child(TreeNode('RAHUL (cloud manager)'))
    infra_head.add_child(TreeNode('SHARAN (App manager)'))

    cto = TreeNode('VIJAY (CTO)')
    cto.add_child(infra_head)
    cto.add_child(TreeNode('NAVEEN (Application head)'))

    hr_head = TreeNode('HARI (HR)')
    hr_head.add_child(TreeNode('PARTHI (Requirement head)'))
    hr_head.add_child(TreeNode('MAGESH (Policy manager)'))

    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__ == '__main__':
    root = build_product_tree()
    root.print()
