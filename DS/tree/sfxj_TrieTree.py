class IntTrie:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


def insert(t, key, value=None):
    if t is None:
        t = IntTrie()
    p = t
    while key:
        if key & 1:
            if p.right is None:
                p.right = IntTrie()
            p = p.right
        else:
            if p.left is None:
                p.left = IntTrie()
            p = p.left
        key >>= 1
    p.value = value
    return t


def lookup(t, key):
    while key and t:
        if key & 1:
            t = t.right
        else:
            t = t.left
        key >>= 1
    if t:
        return t.value
    return None
