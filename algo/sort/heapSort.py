heap = [None, ]


def shiftup(i):
    parent = i // 2
    if parent > 0 and heap[parent] > heap[i]:
        heap[parent], heap[i] = heap[i], heap[parent]
        shiftup(parent)


def shiftdown(i):
    left = i * 2
    right = i * 2 + 1
    minest = i

    if left < len(heap) and heap[left] < heap[minest]:
        minest = left
    if right < len(heap) and heap[right] < heap[minest]:
        minest = right

    if minest != i:
        heap[i], heap[minest] = heap[minest], heap[i]
        shiftdown(minest)


def pop():
    if len(heap) >= 2:
        res = heap[1]
        last = len(heap) - 1

        heap[1] = heap[last]
        heap.pop()
        shiftdown(1)
        return res


def add(val):
    heap.append(val)

    last = len(heap) - 1
    shiftup(last)


if __name__ == '__main__':
    arr = [1, 98, 3, 2, 4, 7, 123]
    [add(i) for i in arr]

    val = pop()
    while val:
        print(val, end=' ')
        val = pop()
