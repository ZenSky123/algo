class DoubleArrayQueue:
    def __init__(self):
        self.front = []
        self.rear = []

    @property
    def empty(self):
        return self.front == [] and self.rear == []

    def push(self, value):
        self.rear.append(value)

    def pop(self):
        if self.front == []:
            self.rear.reverse()
            (self.front, self.rear) = (self.rear, [])
        return self.front.pop()


if __name__ == '__main__':
    q = DoubleArrayQueue()
    [q.push(i) for i in range(10)]

    while not q.empty:
        print(q.pop())
