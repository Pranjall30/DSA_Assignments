class SeparateChainingHashmap:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def find(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False

    def insert(self, key, value):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

# Example usage:
hashmap = SeparateChainingHashmap(10)
hashmap.insert("key1", "value1")
hashmap.insert("key2", "value2")
print(hashmap.find("key1"))  # True
print(hashmap.find("key3"))  # False
hashmap