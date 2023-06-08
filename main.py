import queues

new_queue = queues.Queue(8)

new_queue.enqueue(23)
new_queue.enqueue(78)

print(new_queue.dequeue())

new_queue.enqueue(98)

new_queue.print_queue()
