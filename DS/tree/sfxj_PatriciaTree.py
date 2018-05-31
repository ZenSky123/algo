class IntTree:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prefix = None
        self.mask = None

    def set_children(self, l, r):
        self.left = l
        self.r = r

    def replace_child(self, x, y):
        if self.left == x:
            self.left = y
        else:
            self.right = y

    def is_leaf(self):
        return self.left is None and self.right is None

    def get_prefix(self):
        if self.prefix is None:
            return self.key
        else:
            return self.prefix


def maskbit(x, mask):
    return x & (~(mask - 1))


def match(key, tree):
    return (not tree.is_leaf()) and maskbit(key, tree.mask) == tree.prefix


def zero(x, mask):
    return x & (mask >> 1) == 0


def lcp(p1, p2):
    diff = p1 ^ p2
    mask = 1
    while diff:
        diff >>= 1
        mask <<= 1
    return (maskbit(p1, mask), mask)


def branch(t1, t2):
    t = IntTree()
    t.prefix, t.mask = lcp(t1.get_prefix(), t2.get_prefix())
    if zero(t1.get_prefix(), t.mask):
        t.set_children(t1, t2)
    else:
        t.set_children(t2, t1)
    return t


def insert(t, key, value=None):
    if t is None:
        t = IntTree(key, value)
        return t
    node = t
    parent = None
    while True:
        if match(key, node):
            parent = node
            if zero(key, node.mask):
                node = node.left
            else:
                node = node.right
        else:
            if node.is_leaf() and key == node.key:
                node.value = value
            else:
                new_node = branch(node, IntTree(key, value))
                if parent is None:
                    t = new_node
                else:
                    parent.replace_child(node, new_node)
            break
    return t


def lookup(t, key):
    if t is None:
        return None
    while (not t.is_left()) and match(key, t):
        if zero(key, t.mask):
            t = t.left
        else:
            t = t.right
    if t.is_leaf() and t.key == key:
        return t.value
    else:
        return None
