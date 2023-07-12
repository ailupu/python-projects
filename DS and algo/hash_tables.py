#############  HASH TABLES  ##########
# dictionaries -> perform a has to a key -> to restore the pare in the memory
# put the KEY  in the hash and retrieve VALUE but not the other way aroud
# It is deterministic -> we expect the same value for a specific KEY when put in the hash

# Colission is when you add a key value pair to a memory where it already exists ->  seperate chaining
# you need to go down to find an empty spot
# you can also create a linked list to an adress

# constructor
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size  # creates a list of 7 elements that contain None
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) *23) % len(self.data_map)
                                # ord - gets the ascii number for each letter as we loop - 23 is prime number
                                # % will be 0 to 6 and will be the adresses
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i,":",val)
    
    #set a key value pair in hash table
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    #get all of th keys and put them in the lists and returns it
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

my_hash_table = HashTable()

my_hash_table.set_item('bolts','1400')
my_hash_table.set_item('washers','50')
my_hash_table.set_item('lumber','70')
my_hash_table.print_table()

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('test'))
print(my_hash_table.keys())

#Hash table Big O - for the hash table algh -> O(1)
#                 - setting an item -> O(1)
#                 - get item -> O(1)
