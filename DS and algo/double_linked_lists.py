class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp= temp.next

    #append method
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

        return True
    
    # pop method
    def pop(self):
        if self.head is None:
            return None

        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1

        return temp
    
    #prepend
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
           new_node.next = self.head
           self.head.prev = new_node
           self.head = new_node
        self.length += 1
    
    #pop first
    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    #get method
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
        return temp
    
    # set method 
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    #def insert
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    # remove item at an index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        
        temp.next = None
        temp.prev = None


        self.length -= 1

        return temp


my_d_linked = DoublyLinkedList(7)
my_d_linked.append(5)
my_d_linked.print_list()

print("Pop the eleement")
my_d_linked.pop()
my_d_linked.print_list()

print("Prepend element 1 to the list")
my_d_linked.prepend(1)
my_d_linked.prepend(4)
my_d_linked.prepend(3)
my_d_linked.print_list()

print("Pop first element")
my_d_linked.pop_first()
my_d_linked.print_list()

print("get the value")
print("element found at index 2 is:",my_d_linked.get(2))
print("element found at index 1 is:",my_d_linked.get(1))

print("Change value of link from 1 to 9")
my_d_linked.set_value(1,9)
my_d_linked.print_list()

print("Add new value in the middle of the node")
my_d_linked.insert(1,6)
my_d_linked.print_list()