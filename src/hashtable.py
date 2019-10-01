# '''
# Linked List hash table key/value pair
# '''
import hashlib

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        # print warning
        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        if self.count >= self.capacity:
            self.resize()

        index = self._hash_mod(key)
        entry = self.storage[index]
        
        if entry is None:
            self.storage[index] = LinkedPair(key,value) 

        else:
            prev = entry

            while entry and entry.key != key:
                prev = entry 
                entry = entry.next
                prev.next = LinkedPair(key,value)

            self.count += 1

        # if self.storage[index] is not None:
        #     print('Warning: Index collision')
        #     return
        
        # self.storage[index] = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # try:
        #     self.storage[self._hash_mod(key)] = None
        # except:
        #     print('Warning, key not valid!')

        index = self._hash_mod(key)

        if self.storage[index] is None:
            print('Warning')

        self.storage[index] = None
        self.count -= 1

        

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # try:
        #     return self.storage[self._hash_mod(key)].value
        # except:
        #     return None

        index = self._hash_mod(key)
        pair = self.storage[index]

        if pair is None:
            return None
        else:
            while pair and pair.key != key:
                pair = pair.next
            return pair.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2

        upgradeStore = [None] * self.capacity

        # for i in range(len(self.storage)):
        #     upgradeStore[i] = self.storage[i]

        # self.storage = upgradeStore

        for pair in self.storage:
            if pair is not None:
                new_index = self._hash_mod(pair.key)
                upgradeStore[new_index] = pair

        self.storage = upgradeStore

        

# ht = HashTable(2)

# print(ht._hash_mod('Johnson'))



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
