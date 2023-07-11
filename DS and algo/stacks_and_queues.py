#############  STACKS ############
# You can only get to the last item if you push from up ex: 1-> 2 -> 3 
# to get 1 you have to get out 3 and 2
# LIFO - Last in first out

# To implement: you can use a list - if you add at the end or remove at the end is O(1)
# We can implement the stack as a linked list: pop() and push()

# we will have the last element as top (1) and bottom the first from the stack (3) - we do not need the bottom tho
print("========= STACKS =========")
# Make the constructor:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Create stack
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    # print the value of the node
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    # push a value on the stack
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    # make the pop from the top
    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp

my_stack = Stack(2)
#my_stack.print_stack()

my_stack.push(1)
my_stack.push(3)
my_stack.push(5)
print("Push on the stack")
my_stack.print_stack()

print("Take one elemnt from the top")
my_stack.pop()
my_stack.print_stack()


####################  QUEUES  #############
# First in first out - FIFO
# we want to enqueue last and dequeue from the front because it's O(1)
#head and tail => first and last for queues
print("========= QUEUES =========")
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.first

        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1

        return temp


my_queue = Queue(1)

my_queue.enqueue(2)
my_queue.enqueue(3)
print("Added to the queue")
my_queue.print_queue()

print("Dequeue the first elemnt")
my_queue.dequeue()
my_queue.print_queue()