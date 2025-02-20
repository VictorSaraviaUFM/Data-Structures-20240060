import matplotlib.pyplot as plt
import numpy as np
import time
from Inciso2 import CircularQueue
from Inciso3 import queues
from Inciso4 import search_in_queue 
from Inciso5 import results

n = 10000000

queue_sizes = [n, 2*n, 3*n, 4*n, 5*n]
search_times = [result['search_time'] for result in results]
dequeue_times = [result['dequeue_time'] for result in results]

plt.figure(figsize=(10, 6))

plt.plot(queue_sizes, search_times, marker='o', linestyle='-', color='b', label='Search')
plt.plot(sizes, delete_times, marker='s', linestyle='--', color='r', label='Delete')


plt.xlabel('Elements in millions')
plt.ylabel('Occurrences')
plt.title('Search and Delete Occurrences')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)


plt.show()