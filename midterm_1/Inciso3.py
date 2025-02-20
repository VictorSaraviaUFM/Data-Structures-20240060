from Inciso2 import CircularQueue
from time import time 
import time


n = 1000000

queues = {
    'queue_n': CircularQueue(n),
    'queue_2n': CircularQueue(2 * n),
    'queue_3n': CircularQueue(3 * n),
    'queue_4n': CircularQueue(4 * n),
    'queue_5n': CircularQueue(5 * n)
}

for queue_name, queue in queues.items():
    print(f"Poblando {queue_name}...")

    for i in range(queue.max):
        queue.enqueue(f'Elemento_{i}')  # Poblar con elementos únicos
    print(f"{queue_name} ha sido poblada.\n")