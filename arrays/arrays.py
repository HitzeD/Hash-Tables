# Things we need for an advanced array
# size of it and protection from going past that
# size of objects
# to append need space
# track allocated and used
# if we run out of space, we need to make a new one with space
# then copy each item over


class DynamicArray:

    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * capacity
    
    def append(self, value):

        if self.count >= self.capacity:
            self.resize_array()
        
        self.storage[self.count] = value
        self.count += 1

    def insert(self, value, index):

        if self.count >= self.capacity:
            self.resize_array()

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]

        self.storage[index] = value
        self.count += 1

    def remove(self, index):

        # 3 find the index we want
        value = self.storage[index]

        # replace with the next value and move down list until end
        for i in range(index, self.count - 1, 1):
            self.storage[i] = self.storage[i + 1]

        # subtract from count
        self.count -= 1

        # resize?

        # Do we need to return it?
        return value

    def print(self):
        for value in self.storage:
            print(value)
    

    def resize_array(self):
        self.capacity *= 2
        
        newStorage = [None] * self.capacity

        for i in range(self.count):
            newStorage[i] = self.storage[i]

        self.storage = newStorage

    def add_to_front(self, value):
        self.insert(value, 0)
