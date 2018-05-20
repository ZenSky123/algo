class CircularQueue:
    def __init__(self, max_size):
        self.queue = [0] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0
        self.max_size = max_size

    @property
    def full(self):
        return self.size == self.max_size

    @property
    def empty(self):
        return self.size == 0

    def enqueue(self, value):
        if self.full:
            raise TypeError('The queue is full!')

        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        if self.empty:
            raise TypeError('The queue is empty!')

        value = self.queue[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

        return value


if __name__ == '__main__':
    q = CircularQueue(10)

    [q.enqueue(i) for i in range(5)]
    while not q.empty:
        print(q.dequeue())

    [q.enqueue(i) for i in range(11)]  # Error!
