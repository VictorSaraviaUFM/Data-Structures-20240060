from memory_profiler import profile
import numpy as np
import time 
from Inciso2 import CircularQueue
from Inciso3 import queues

n = 10000000

@profile
def search_in_queue(queue: CircularQueue, key: str) -> int:
    if queue.is_empty():
        print('La cola se encuentra vacía.')
        return False

    current = queue.front
    position = 0

    while True:
        if queue.elements[current] == key:
            return position

        if current == queue.rear:
            break

        current = (current + 1) % queue.max
        position += 1

    print(f'El elemento "{key}" no se encontró en la cola.')
    return False