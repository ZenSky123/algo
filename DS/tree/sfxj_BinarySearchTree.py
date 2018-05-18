class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def pre_order_walk(node):
    if node is not None:
        print(node.value, end=' ')
        pre_order_walk(node.left)
        pre_order_walk(node.right)


def in_order_walk(node):
    if node is not None:
        in_order_walk(node.left)
        print(node.value, end=' ')
        in_order_walk(node.right)


def post_order_walk(node):
    if node is not None:
        post_order_walk(node.left)
        post_order_walk(node.right)
        print(node.value, end=' ')


def RecursionInsert(node, value):
    if value < node.value:
        if node.left is None:
            node.left = Node(value)
            node.left.parent = node
        else:
            RecursionInsert(node.left, value)
    else:
        if node.right is None:
            node.right = Node(value)
            node.right.parent = node
        else:
            RecursionInsert(node.right, value)


def NonRecursionInsert(node, value):
    root = node
    x = Node(value)
    parent = None

    while node is not None:
        parent = node
        if value < parent.value:
            t = t.left
        else:
            t = t.right

    x.parent = parent

    if parent is None:
        return x
    elif value < parent.value:
        parent.left = x
    else:
        parent.right = x

    return root


def lookup(node, value):
    if node is None:
        return None
    if value < node.value:
        return lookup(node.left, value)
    if value > node.value:
        return lookup(node.right, value)
    return node


def Min(node):
    if node.left:
        return Min(node.left)
    return node


def Max(node):
    if node.right:
        return Max(node.right)
    return node


def succ(node):
    if node.right:
        return min(node.right)

    parent = node.parent

    while parent is not None and parent.right == node:
        node = parent
        parent = parent.parent
    return parent


def pred(node):
    if node.left:
        return max(node.left)
    parent = node.parent
    while parent is not None and parent.left == node:
        node = parent
        parent = parent.parent
    return parent


def Delete(node, x):
    if not isinstance(x, Node):
        x = lookup(node, x)
    if x is None:
        return node
    root, old_x, parent = (node, x, x.parent)

    if x.left is None:
        x = x.right
    elif x.right is None:
        x = x.left
    else:
        y = Min(x.right)
        x.value = y.value
        if y.parent != x:
            y.parent.left = y.right
        else:
            x.right = y.right
        return root
    if x is not None:
        x.parent = parent
    if parent is None:
        root = x
    else:
        if parent.left == old_x:
            parent.left = x
        else:
            parent.right = x
    return root


if __name__ == '__main__':
    node = Node(10)
    RecursionInsert(node, 11)
    RecursionInsert(node, 1)
    RecursionInsert(node, 5)
    RecursionInsert(node, 9)
