# Linked lists does not have indexes like a normal list
# Is placed in a contiguous place in memory 
#   - data is next to each other in memory
# We have a head - first item in the list
#           tail - last item in the list

"""Link list BIG O:
                - append : O(1) -> tail changes
                - remove : you have to start with head iterate to every node 
                        until the last one and tail will change => O(n)
                - add item at the front : O(1)
                - removing first note : move head next and remove item => O(1)
                - adding an item somewhere in middle : iterate the list => O(n)
                - removig a node in the middle: iterate the list => O(n)
                - lookup for a node : iterate => O(n)
"""            
# a node is a value with the pointer - is similar to a dictionary

head = { "value": 11,
         "next":{
             "value": 3,
             "next": {
                 "value":23,
                 "next": {
                     "value": 7,
                     "next": None
                 }
             }
         }

}
print(head["next"]["next"]["value"])

#Constructor

#class LinkedList:
    #def __init__(self, value):
        # CREATE A NEW NODE
        #self.value = value
    #def append(self,value):
        # CREATE A NEW NODE AND ADD TO END
    #def prepend(self,value):
        # CREATE A NEW NODE AND ADD AT BEGINNING
    #def insert(self, index, value):
        # CREATE NEW NODE AND INSERT

# Instead of cerating 4 functions to create node we create only one class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True
    
    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
            
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.head
        for _ in range(index):
            temp = temp.next   #or self.get(index) with no for
        
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next=temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        after = temp.next
        before = None
        self.head = self.tail
        self.tail = temp
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


#Create linked list
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(11)
my_linked_list.append(5)
print("Before pop")
my_linked_list.print_list()

my_linked_list.pop()
print("After pop")
my_linked_list.print_list()

print('Prepend')
my_linked_list.prepend(3)
my_linked_list.print_list()

print("Pop first item")
my_linked_list.pop_first()
my_linked_list.print_list()

print(my_linked_list.get(1))

print("Set value")
my_linked_list.set_value(1,4)
my_linked_list.print_list()

print("Insert node")
my_linked_list.insert(2,6)
my_linked_list.print_list()

print("Remove the intem at index 2")
my_linked_list.remove(2)
my_linked_list.print_list()

print("Make linked list reversed")
my_linked_list.reverse()
my_linked_list.print_list()