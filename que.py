import time
import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def simulate_line(till_show, max_time):
    queue = Queue()
    ticket_sold = []

    for i in range(100):
        queue.enqueue("person" + str(i))

    t_end = time.time() + till_show
    now = time.time()
    while now < t_end and not queue.is_empty():
        now = time.time()
        random_duration = random.randint(0, max_time)
        time.sleep(random_duration)
        person = queue.dequeue()
        print(person)
        ticket_sold.append(person)

    return ticket_sold


sold = simulate_line(5, 1)
print(sold)
