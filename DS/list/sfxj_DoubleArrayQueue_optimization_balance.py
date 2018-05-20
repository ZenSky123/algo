'''
    To balance the length of thw two array ( [front] and [rear] )
    Add a restrictive condition :
        reverse the [rear] when len(rear)>len(front)
'''


class DoubleArrayQueue:
    def __init__(self):
        self.front = []
        self.rear = []
        self.front_length = 0
        self.rear_length = 0

    @property
    def empty(self):
        return self.front == [] and self.rear == []

    def push(self, value):
        self.rear.append(value)
        self.rear_length += 1

        self._balance()

    def pop(self):
        value = self.front.pop()
        self.front_length -= 1

        self._balance()

        return value

    @property
    def _need_balance(self):
        return self.rear_length > self.front_length

    def _balance(self):
        if self._need_balance:
            self.rear.reverse()
            self.rear.extend(self.front)

            self.front, self.rear = self.rear, []
            self.front_length += self.rear_length
            self.rear_length = 0


if __name__ == '__main__':
    q = DoubleArrayQueue()
    [q.push(i) for i in range(10)]

    while not q.empty:
        print(q.pop())
