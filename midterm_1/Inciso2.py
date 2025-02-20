import time

class CircularQueue:
    def __init__(self, size: int):
        self.max = size
        self.elements = [None] * size
        self.front = -1
        self.rear = -1

    def __repr__(self) -> str:
        return f'Queue: {self.elements} | F: {self.front} | R: {self.rear}'

    def is_full(self) -> bool:
        return (self.rear + 1) % self.max == self.front

    def is_empty(self) -> bool:
        return self.front == -1

    def enqueue(self, val: str) -> None:
        if self.is_full():
            print('Queue overflow...')
            return None

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max

        self.elements[self.rear] = val

    def dequeue(self) -> str:
        if self.is_empty():
            print('Queue Underflow...')
            return None

        val = self.elements[self.front]
        self.elements[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max

        return val



