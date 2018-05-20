import random

MIN_HEAP = lambda a, b: a < b
MAX_HEAP = lambda a, b: a > b


def parent(index):
    return index // 2 - 1


def left(index):
    return 2 * index + 2


def right(index):
    return 2 * (index + 1)


def heapify(arr, index, compare=MIN_HEAP):
    n = len(arr)
    while 1:
        l = left(index)
        r = right(index)
        mark = index

        if l < n and compare(arr[l], arr[index]):
            mark = l
        if r < n and compare(arr[r], arr[index]):
            mark = r

        if mark != index:
            arr[mark], arr[index] = arr[index], arr[mark]
            index = mark
        else:
            break


def build_heap(arr, compare=MIN_HEAP):
    n = len(arr)
    for index in reversed(range(n // 2)):
        heapify(arr, index, compare)


def top(arr):
    return arr[0]


def pop(arr, compare=MIN_HEAP):
    value = top(arr)
    arr[0] = arr[-1]
    arr.pop()
    if arr:
        heapify(arr, 0, compare)
    return value


def sort(arr, compare=MIN_HEAP):
    build_heap(arr, compare)

    res = []
    while arr:
        res.append(pop(arr, compare))

    return res


def decrease(arr, index, key, compare=MIN_HEAP):
    if compare(key, arr[index]):
        arr[index] = key
        fix(arr, index, compare)


def insert(arr, key, compare=MIN_HEAP):
    n = len(arr)
    arr.append(key)
    fix(arr, n, compare)


def fix(arr, index, compare=MIN_HEAP):
    while index and compare(arr[index], arr[parent(index)]):
        arr[parent(index)], arr[index] = arr[index], arr[parent(index)]
        index = parent(index)


def top_k(arr, k, compare=MIN_HEAP):
    build_heap(arr, compare)
    return [pop(arr, compare) for _ in range(min(k, len(arr)))]


if __name__ == '__main__':
    heap=[random.randint(1,1000) for _ in range(20)]

    print(heap)
    print(sort(heap))
