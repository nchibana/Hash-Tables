# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, key, value):
        if self.head == None:
            self.head = LinkedPair(key, value)
        else:
            placeholder = self.head
            self.head = LinkedPair(key, value)
            self.head.next = placeholder

    def contains(self, key):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def remove(self, key):
        if not self.head:
            print("Error: Key not found")
        elif self.head.key == key:
            # Remove head
            self.head = self.head.next
        else:
            parent = self.head
            current = self.head.next
            while current:
                if current.key == key:
                    # Remove node
                    parent.next = current.next
                    return
                current = current.next
            print("Error: Key not found")

    def retrieve(self, key):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return False


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


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

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)
        
        if self.storage[hashed_key] is not None:
            self.storage[hashed_key].add_to_head(key, value)

        else:
            sll = LinkedList()
            sll.add_to_head(key, value)
            self.storage[hashed_key] = sll


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)

        if self.storage[hashed_key] is not None:
            self.storage[hashed_key].remove(key)
        else:
            print("Key not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)

        if self.storage[hashed_key] is not None:
            if self.storage[hashed_key].retrieve(key) is not False:
                return self.storage[hashed_key].retrieve(key).value
            else:
                return None
        else:
           return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2

        nodes = []

        for i in range(len(self.storage)):
            if self.storage[i] is not None:
                parent = self.storage[i].head
                nodes.append((parent.key, parent.value))
                current = self.storage[i].head.next
                while current:
                    nodes.append((current.key, current.value))
                    current = current.next
        
        self.storage = [None] * self.capacity

        for i in range(len(nodes)):
            self.insert(nodes[i][0], nodes[i][1])


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
