class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,data):
        new = Node(data)
        if self.tail is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def dequeue(self):
        if self.head is None:
            self.tail = None
            return
        removed = self.head.data
        self.head = self.head.next
        return removed
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(3)
my_queue.enqueue(6)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())