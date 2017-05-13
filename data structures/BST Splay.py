import sys

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
        return "{}|p{}".format(self.value, self.parent.value if self.parent else None)


class BST:
    def __init__(self, root: Node):
        self.root = root

    def __repr__(self):
        result = """
                               {}
                          /             \\
                   {}                {}
                 /      \\               /      \\
             {}       {}          {}      {}
            /    \\      /   \\         /   \\      /   \\
          {}  {} {}  {}   {}  {} {}  {}

        """
        EMPTY = "    "
        all_nodes = []
        this_level = [self.root]
        while any([x for x in this_level if x != EMPTY]):
            next_level = []
            for n in this_level:
                all_nodes.append(n)
                next_level.append(n.left if n != EMPTY and n.left else EMPTY)
                next_level.append(n.right if n != EMPTY and n.right else EMPTY)
            this_level = next_level
        if len(all_nodes) == 31: result += "{} " * 16
        if len(all_nodes) == 7: result = result[:220]
        if len(all_nodes) == 3: result = result[:120]
        if len(all_nodes) == 1: result = result[:80]
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
                    self.splay(new_node)
                    break

            if new_node > cur_node:
                if cur_node.right:
                    cur_node = cur_node.right
                    continue
                else:
                    cur_node.right = new_node
                    new_node.parent = cur_node
                    self.splay(new_node)
                    break

    def zig(self, x: Node):
        print(sys._getframe().f_code.co_name)
        p = x.parent
        x.parent = p.parent
        p.parent = x
        p.left = x.right
        if x.right: x.right.parent = p
        x.right = p

    def zag(self, x: Node):
        print(sys._getframe().f_code.co_name)
        p = x.parent
        x.parent = p.parent
        p.parent = x
        p.right = x.left
        if x.left: x.left.parent = p
        x.left = p

    def zigzig(self, x: Node):
        print(sys._getframe().f_code.co_name)
        p = x.parent
        g = p.parent

        if g.parent:
            if g == g.parent.left:
                g.parent.left = x
            else:
                g.parent.righ = x
        x.parent = g.parent

        p.left = x.right
        x.right = p
        p.parent = x

        g.left = p.right
        p.right = g
        g.parent = p

    def zagzag(self, x: Node):
        print(sys._getframe().f_code.co_name)
        p = x.parent
        g = p.parent

        if g.parent:
            if g == g.parent.left:
                g.parent.left = x
            else:
                g.parent.righ = x
        x.parent = g.parent

        p.right = x.left
        x.left = p
        p.parent = x

        g.right = p.left
        p.left = g
        g.parent = p

    def zigzag(self, x: Node):
        print(sys._getframe().f_code.co_name)
        p = x.parent
        g = p.parent

        if g.parent:
            if g == g.parent.left:
                g.parent.left = x
            else:
                g.parent.right = x
        x.parent = g.parent

        p.right = x.left
        x.left = p
        p.parent = x

        g.left = x.right
        x.right = g
        g.parent = x

    def zagzig(self, x: Node):
        print(sys._getframe().f_code.co_name)
        p = x.parent
        g = p.parent

        if g.parent:
            if g == g.parent.left:
                g.parent.left = x
            else:
                g.parent.righ = x
        x.parent = g.parent
        print('g.parent = ', x.parent)

        p.left = x.right
        x.right = p
        p.parent = x

        g.right = x.left
        x.left = g
        g.parent = x

    def splay(self, x_node: Node):
        if not x_node.parent:
            return

        while x_node.parent:
            if x_node.parent.parent:
                if x_node == x_node.parent.left and x_node.parent == x_node.parent.parent.left:
                    self.zigzig(x_node)
                elif x_node == x_node.parent.right and x_node.parent == x_node.parent.parent.right:
                    self.zagzag(x_node)
                elif x_node == x_node.parent.right and x_node.parent == x_node.parent.parent.left:
                    self.zigzag(x_node)
                elif x_node == x_node.parent.left and x_node.parent == x_node.parent.parent.right:
                    self.zagzig(x_node)
            else:
                if x_node == x_node.parent.left:
                    self.zig(x_node)
                elif x_node == x_node.parent.right:
                    self.zag(x_node)

        bst.root = x_node

    def search(self, x: Node) -> bool:
        cur_node = bst.root
        while True:
            if not cur_node:
                return False
            if x == cur_node:
                self.splay(cur_node)
                return True

            cur_node = cur_node.left if x < cur_node else cur_node.right


bst = BST(Node(6))
bst.add(Node(8))
bst.add(Node(10))
bst.add(Node(9))
bst.add(Node(12))
bst.add(Node(11))

bst.search(Node(8))
bst.search(Node(10))
bst.search(Node(11))


print(bst)

