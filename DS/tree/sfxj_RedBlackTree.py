from enum import Enum

Color = Enum('Color', ['BLACK', 'RED', 'DOUBLE_BLACK'])
RED = Color.RED
BLACK = Color.BLACK
DOUBLE_BLACK = Color.DOUBLE_BLACK


class Node:
    def __init__(self, key, color=RED):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color

    def set_left(self, x):
        self.left = x
        if x:
            x.parent = self

    def set_right(self, x):
        self.right = x
        if x:
            x.parent = self

    def set_children(self, x, y):
        self.set_left(x)
        self.set_right(y)

    def replace(self, y):
        if self.parent is None:
            if y is not None:
                y.parent = None
        elif self.parent.left is self:
            self.parent.set_left(y)
        else:
            self.parent.set_right(y)
        self.parent = None

    def sibling(self):
        if self.parent.left is self:
            return self.parent.right
        else:
            return self.parent.left

    def uncle(self):
        return self.parent.sibling()

    def grandparent(self):
        return self.parent.parent


def set_color(nodes, colors):
    for node, color in zip(nodes, colors):
        node.color = color


# (a x (b y c)) ==> ((a x b) y c)
def left_rotate(t, x):
    parent, y = (x.parent, x.right)
    a, b, c = (x.left, y.left, y.right)
    x.replace_by(y)
    x.set_children(a, b)
    y.set_children(x, c)
    if parent is None:
        t = y
    return t


# ((a x b) y c) ==> (a x (b y c))
def right_rotate(x, y):
    parent, x = (y.parent, y.left)
    a, b, c = (x.left, x.right, y.right)
    y.replace_by(x)
    y.set_children(b, c)
    x.set_children(a, y)
    if parent is None:
        t = x
    return t


def insert(t, key):
    root = t
    x = Node(key)
    parent = None

    while t:
        parent = t
        if key < t.key:
            t = t.left
        else:
            t = t.right
    if parent is None:
        root = x
    elif key < parent.key:
        parent.set_left(x)
    else:
        parent.set_right(x)
    return insert_fix(root, x)


def insert_fix(t, x):
    while x.parent and x.parent.color == RED:
        if x.uncle().color == RED:
            set_color([x.parent, x.grandparent(), x.uncle()],
                      [BLACK, RED, BLACK])
            x = x.grandparent()
        else:
            if x.parent == x.grandparent().left:
                if x is x.parent.right:
                    x = x.parent
                    t = left_rotate(t, x)
                set_color([x.parent, x.grandparent()],
                          [BLACK, RED])
                t = right_rotate(t, x.grandparent())
            else:
                if x is x.parent.left:
                    x = x.parent
                    t = right_rotate(t, x)
                set_color([x.parent, x.grandparent()],
                          [BLACK, RED])
                t = left_rotate(t, x.grandparent())
    t.color = BLACK
    return t


def search(t, x):
    while t and t.key != x:
        if x < t.key:
            t = t.left
        else:
            t = t.right
    return t


def min(t):
    while t and t.left:
        t = t.left
    return t


def remove(x):
    if x is None:
        return
    x.parent = None
    x.left = None
    x.right = None


def is_leaf(x):
    if x is None:
        return False
    return (x.left is None) and (x.right is None)


def make_black(parent, x):
    if x is None:
        if is_leaf(parent):
            parent.color = DOUBLE_BLACK
        return parent
    else:
        x.color = {
            RED: BLACK,
            BLACK: DOUBLE_BLACK
        }[x.color]
        return x


def delete(t, x):
    if x is None:
        return t
    parent, db = (x.parent, None)
    if x.left is None:
        x.replace_by(x.right)
        db = x.right
    elif x.right is None:
        x.replace_by(x.left)
        db = x.left
    else:
        y = min(x.right)
        parent, db = (y.parent, y.right)
        x.key = y.key
        y.replace_by(y.right)
        x = y
    if x.color == BLACK:
        t = delete_fix(t, make_black(parent, db))
    remove(x)
    return t


def is_red(x):
    if x is None:
        return False
    return x.color == RED


def is_black(x):
    if x is None:
        return False
    return x.color == BLACK


def delete_fix(t, db):
    if db is None:
        return None
    while (db is not t) and (db.color == DOUBLE_BLACK):
        if db.sibling() != None:
            if is_red(db.sibling()):
                set_color([db.parent, db.sibling()],
                          [RED, BLACK])
                if db is db.parent.left:
                    t = left_rotate(t, db.parent)
                else:
                    t = right_rotate(t, db.parent)
            elif is_black(db.sibling()) and is_red(db.sibling().left):
                if db is db.parent.left:
                    colors = [BLACK, BLACK, db.parent.color]
                    set_color([db, db.parent, db.sibling().left],
                              colors)
                    t = right_rotate(t, db.sibling())
                    t = left_rotate(t, db.parent)
                else:
                    colors = [BLACK, BLACK, db.parent.color, BLACK]
                    set_color([db, db.parent, db.sibling(), db.sibling().left],
                              colors)
                    t = right_rotate(t, db.parent)
            elif is_black(db.sibling()) and is_red(db.sibling().right):
                if db == db.parent.left:
                    colors = [BLACK, BLACK, db.parent.color, BLACK]
                    set_color([db, db.parent, db.sibling(), db.sibling().right], colors)
                    t = left_rotate(t, db.parent)
                else:
                    colors = [BLACK, BLACK, db.parent.color]
                    set_color([db, db.parent, db.sibling().right],
                              colors)
                    t = left_rotate(t, db.sibling())
                    t = right_rotate(t, db.parent)
            elif is_black(db.sibling()) and (not is_red(db.sibling().right)):
                set_color([db, db.sibling()],
                          [BLACK, RED])
                db.parent.color = {
                    RED: BLACK,
                    BLACK: DOUBLE_BLACK
                }[db.parent.color]
                db = db.parent
        else:
            db.color = BLACK
            db.parent.color = {
                RED: BLACK,
                BLACK: DOUBLE_BLACK
            }[db.parent.color]
            db = db.parent
    t.color = BLACK
    return t


if __name__ == '__main__':
    x = Node(11)
    x = insert(x, 2)
    x = insert(x, 11)
    x = insert(x, 1)
    x = insert(x, 7)
    x = insert(x, 5)
    x = insert(x, 8)
    x = insert(x, 14)
    x = insert(x, 15)
