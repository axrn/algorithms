class Node:
    __slots__ = ["value", "parent", "left", "right", "height"]

    def __init__(self, value: int) -> None:
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1

    def __lt__(self, other: 'Node') -> bool:
        return self.value < other.value

    def __gt__(self, other: 'Node') -> bool:
        return self.value > other.value

    def __eq__(self, other: 'Node') -> bool:
        if not isinstance(other, Node):
            return False
        return self.value == other.value

    def __repr__(self) -> str:
        return "{}|h{}".format(self.value, self.height)


class BST:
    def __init__(self, root: Node):
        self.root = root

    def __repr__(self):
        result = """
                               {}
                          /             \\
                    {}                 {}
                 /      \\               /      \\
             {}       {}          {}     {}
            /   \\      /   \\         /   \\     /    \\
        {}   {}  {}  {}   {}  {} {}  {}

        """
        all_nodes = []
        this_level = [self.root]
        while any(this_level):
            next_level = []
            for n in this_level:
                all_nodes.append(n)
                next_level.append(n.left if n and n.left else None)
                next_level.append(n.right if n and n.right else None)
            this_level = next_level
        if len(all_nodes) == 31: result += "{} " * 16
        if len(all_nodes) == 7: result = result[:220]
        if len(all_nodes) == 3: result = result[:120]
        if len(all_nodes) == 1: result = result[:80]
        print(all_nodes)
        return result.format(*all_nodes)

    def add(self, new_node: Node) -> None:
        cur_node = self.root
        while True:
            if new_node == cur_node:
                return

            if new_node < cur_node:
                if cur_node.left:
                    cur_node = cur_node.left
                    continue
                else:
                    cur_node.left = new_node
                    new_node.parent = cur_node
                    self.__height_update(new_node)
                    break

            if new_node > cur_node:
                if cur_node.right:
                    cur_node = cur_node.right
                    continue
                else:
                    cur_node.right = new_node
                    new_node.parent = cur_node
                    self.__height_update(new_node)
                    break

    def __height_update(self, added_node: Node):
        print(" from ", added_node)
        if added_node.parent.left and added_node.parent.right:
            return

        parent = added_node.parent
        while parent:
            left_subtree_height = parent.left.height if parent.left else 0
            right_subtree_height = parent.right.height if parent.right else 0
            if abs(left_subtree_height - right_subtree_height) > 1:
                self.balance(parent)
                if added_node.value == 11:
                    print(self.__repr__())
                continue
            parent.height = max(left_subtree_height, right_subtree_height) + 1
            parent = parent.parent

    def is_left_heavy(self, node: Node, diff: int = 2) -> bool:
        if node is None: return False
        left_subtree_height = node.left.height if node.left else 0
        right_subtree_height = node.right.height if node.right else 0
        return left_subtree_height - right_subtree_height >= diff

    def is_right_heavy(self, node: Node, diff: int = 2) -> bool:
        if node is None: return False
        left_subtree_height = node.left.height if node.left else 0
        right_subtree_height = node.right.height if node.right else 0
        return right_subtree_height - left_subtree_height >= diff

    def balance(self, node):
        if self.is_right_heavy(node):
            if self.is_left_heavy(node.right, 1):
                self.double_left_rotate(node)
            else:
                self.left_rotate(node)
        elif self.is_left_heavy(node):
            if self.is_right_heavy(node.left, 1):
                self.double_right_rotate(node)
            else:
                self.right_rotate(node)

    def double_left_rotate(self, node: Node):
        if node.parent is None:
            bst.root = node.right.left

        a = node
        c = a.right
        b = c.left

        b.parent = a.parent
        a.parent = b
        b.left = a
        a.right = None

        c.left = None
        c.parent = b
        c.left = b.right
        b.right = c

        a.height -= 2
        c.height -= 1

    def double_right_rotate(self, node: Node):
        if node.parent is None:
            bst.root = node.left.right

        a = node
        c = a.left
        b = c.right

        b.parent = a.parent
        a.parent = b
        b.right = a
        a.left = None

        c.right = None
        c.parent = b
        c.right = b.left
        b.left = c

        a.height -= 2
        c.height -= 1

    def left_rotate(self, node: Node):
        if not node.parent:
            node.right.parent = None
            self.root = node.right
        elif node.parent.left == node:
            node.parent.left = node.right
            node.right.parent = node.parent
        elif node.parent.right == node:
            node.parent.right = node.right
            node.right.parent = node.parent

        node.right.left = node
        node.parent = node.right
        node.right = None
        node.height -= 2

    def right_rotate(self, node: Node):
        if not node.parent:
            node.left.parent = None
            self.root = node.left
        elif node.parent.right == node:
            node.parent.right = node.left
            node.left.parent = node.parent
        elif node.parent.left == node:
            node.parent.left = node.left
            node.left.parent = node.parent

        node.left.right = node
        node.parent = node.left
        node.left = None
        node.height -= 2


bst = BST(Node(10))
bst.add(Node(5))
bst.add(Node(7))
bst.add(Node(53))
bst.add(Node(76))
bst.add(Node(23))
bst.add(Node(1))
bst.add(Node(15))
print(bst)
# bst.add(Node(11))
# bst.add(Node(8))

# bst.add(Node(9))
# bst.add(Node(8))
# bst.add(Node(7))
# bst.add(Node(6))

# print(bst)

