import time
from Inciso3 import queues
from Inciso4 import search_in_queue

results = []

for queue_name, queue in queues.items():
    print(f"\nOperaciones en {queue_name}:")

    start_time = time.time()
    search_result = search_in_queue(queue, 'No_existe')  
    elapsed_time = time.time() - start_time
    print(f"Búsqueda en {queue_name} ha tenido una duración de {elapsed_time} segundos.")

    # Dequeue
    start_time = time.time()
    dequeued_element = queue.dequeue()
    elapsed_time = time.time() - start_time
    print(f"Dequeue en {queue_name} ha tomado {elapsed_time} segundos.")
    print(f"Elemento eliminado es: {dequeued_element}")

    results.append({
        'queue_name': queue_name,
        'search_time': elapsed_time,
        'dequeue_time': elapsed_time
    })

print("\nResultados:")
for result in results:
    print(f"{result['queue_name']}: Búsqueda tomó {result['search_time']} segundos, Dequeue tomó {result['dequeue_time']} segundos.")