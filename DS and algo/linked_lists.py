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
    
    #def pop(self):




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()