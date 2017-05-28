class Node:
    __slots__ = ["value", "parent", "left", "right"]

    def __init__(self, value: int) -> None:
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def __lt__(self, other: 'Node') -> bool:
        return self.value < other.value

    def __gt__(self, other: 'Node') -> bool:
        return self.value > other.value

    def __eq__(self, other: 'Node') -> bool:
        if not isinstance(other, Node):
            return False
        return self.value == other.value

    def __repr__(self) -> str:
        r_or_l = ""
        p = None
        if self.parent:
            p = self.parent.value
            r_or_l = "lc" if self == self.parent.left else "rc"
        return "{}|{}{}".format(self.value, r_or_l, p)


class BST:
    def __init__(self, root: Node):
        self.root = root
        if self.root is not None:
            self.root.parent = None

    def __repr__(self):
        result = """
                               {}
                          /              \\
                   {}                 {}
                 /      \\                /      \\
             {}      {}         {}    {}
            /    \\      /   \\         /   \\      /   \\
        {}  {} {} {}  {}  {} {} {}

        """
        EMPTY = "     "
        all_nodes = []
        this_level = [self.root]
        while any([x for x in this_level if x != EMPTY]):
            next_level = []
            for n in this_level:
                all_nodes.append(n)
                next_level.append(n.left if n != EMPTY and n.left else EMPTY)
                next_level.append(n.right if n != EMPTY and n.right else EMPTY)
            this_level = next_level
        if len(all_nodes) == 31: result += "{}" * 16
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

    def splay(self, x_node: Node):

        if not x_node.parent:
            return

        while x_node.parent:
            if x_node.parent.parent:
                if x_node == x_node.parent.left and x_node.parent == x_node.parent.parent.left:
                    BST.zigzig(x_node)
                elif x_node == x_node.parent.right and x_node.parent == x_node.parent.parent.right:
                    BST.zagzag(x_node)
                elif x_node == x_node.parent.right and x_node.parent == x_node.parent.parent.left:
                    BST.zigzag(x_node)
                elif x_node == x_node.parent.left and x_node.parent == x_node.parent.parent.right:
                    BST.zagzig(x_node)
            else:
                if x_node == x_node.parent.left:
                    BST.zig(x_node)
                elif x_node == x_node.parent.right:
                    BST.zag(x_node)

        self.root = x_node

    def search(self, x: Node) -> bool:
        cur_node = self.root
        while True:
            if not cur_node:
                return False
            if x == cur_node:
                self.splay(cur_node)
                return True

            cur_node = cur_node.left if x < cur_node else cur_node.right

    def min(self):
        if self.root is None:
            return
        leftest = self.root
        while leftest.left:
            leftest = leftest.left
        return leftest

    def max(self):
        if self.root is None:
            return
        rightest = self.root
        while rightest.right:
            rightest = rightest.right
        return rightest

    def merge(self, second: 'BST'):
        if self.max() < second.min():
            self.splay(self.max())
            self.root.right = second.root
            second.root.parent = self.root
        else:
            second.splay(second.max())
            second.root.right = self.root
            self.root.parent = second.root
            self.root = second.root

    def delete(self, x: Node):
        self.search(x)
        left = self.root.left
        right = self.root.right

        if left is None and right is None:
            self.root = None
            return
        if left is None:
            self.root = right
            self.root.parent = None
            return
        if right is None:
            self.root = left
            self.root.parent = None
            return

        self.root = left
        self.root.parent = None
        self.merge(BST(right))

    @staticmethod
    def zig(x: Node):
        p = x.parent
        x.parent = p.parent
        p.parent = x
        p.left = x.right
        if x.right: x.right.parent = p
        x.right = p

    @staticmethod
    def zag(x: Node):
        p = x.parent
        x.parent = p.parent
        p.parent = x
        p.right = x.left
        if x.left: x.left.parent = p
        x.left = p

    @staticmethod
    def zigzig(x: Node):
        p = x.parent
        g = p.parent

        if g.parent:
            if g == g.parent.left:
                g.parent.left = x
            else:
                g.parent.right = x
        x.parent = g.parent

        p.left = x.right
        if x.right: x.right.parent = p
        x.right = p
        p.parent = x

        g.left = p.right
        if p.right: p.right.parent = g
        p.right = g
        g.parent = p

    @staticmethod
    def zagzag(x: Node):
        p = x.parent
        g = p.parent

        if g.parent:
            if g == g.parent.left:
                g.parent.left = x
            else:
                g.parent.right = x
        x.parent = g.parent

        p.right = x.left
        if x.left: x.left.parent = p
        x.left = p
        p.parent = x

        g.right = p.left
        if p.left: p.left.parent = g
        p.left = g
        g.parent = p

    @staticmethod
    def zigzag(x: Node):
        p = x.parent
        g = p.parent

        if g.parent:
            if g == g.parent.left:
                g.parent.left = x
            else:
                g.parent.right = x
        x.parent = g.parent

        p.right = x.left
        if x.left: x.left.parent = p
        x.left = p
        p.parent = x

        g.left = x.right
        if x.right: x.right.parent = g
        x.right = g
        g.parent = x

    @staticmethod
    def zagzig(x: Node):
        p = x.parent
        g = p.parent

        if g.parent:
            if g == g.parent.left:
                g.parent.left = x
            else:
                g.parent.right = x
        x.parent = g.parent

        p.left = x.right
        if x.right: x.right.parent = p
        x.right = p
        p.parent = x

        g.right = x.left
        if x.left: x.left.parent = g
        x.left = g
        g.parent = x


