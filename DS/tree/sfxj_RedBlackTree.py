from enum import Enum

Color=Enum('Color',['BLACK','RED'])

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color=Color.BLACK


def left_rotate(t, x):
    p = x.parent
    y = x.right
    a = x.left
    b = y.left
    c = y.right

    replace(x, y)
    set_children(x, a, b)
    set_children(y, x, c)
    if p is None:
        t = y
    return t

def right_rotate(t,y):
    p=y.parent
    x=y.left
    a=x.left
    b=x.right
    c=y.right
    replace(y,x)
    set_children(y,b,c)
    set_children(x,a,y)
    if p is None:
        t=x
    return t


def set_left(x, y):
    x.left = y
    if y is not None:
        y.parent = x


def set_right(x, y):
    x.right = y
    if y is not None:
        y.parent = x


def set_children(x, l, r):
    set_left(x, l)
    set_right(x, r)


def replace(x, y):
    if x.parent is None:
        if y is not None:
            y.parent = None
    elif x.parent.left == x:
        set_left(x.parent, y)
    else:
        set_right(x.parent, y)
    x.parent = None

def pre_order_walk(node):
    if node is not None:
        print(node.value,end=' ')
        pre_order_walk(node.left)
        pre_order_walk(node.right)

if __name__ == '__main__':
    x=Node('X')
    x.left=Node('a')
    x.right=Node('Y')
    x.right.left=Node('b')
    x.right.right=Node('c')

    pre_order_walk(x)
    print()
    x=left_rotate(x,x)
    pre_order_walk(x)