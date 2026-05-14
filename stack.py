class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack is Empty")
            return None
        else:
            current = self.head
            self.head = current.next
            return current.data

    def peek(self):
        if self.head is None:
            print("Stack is Empty")
        else:
            first = self.head
            print(first.data)

my_stack = Stack()
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)
my_stack.peek()      # what's on top?
print(my_stack.pop())  # remove top and print it
my_stack.peek()