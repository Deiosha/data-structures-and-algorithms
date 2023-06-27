class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * self.size

    def _hash(self, key):
        """Hashes the key and returns the index of the bucket."""
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def set(self, key, value):
        """Sets the value associated with the given key in the hashtable."""
        index = self._hash(key)
        if self._buckets[index] is None:
            self._buckets[index] = []
        for item in self._buckets[index]:
            if item[0] == key:
                item[1] = value
                return
        self._buckets[index].append([key, value])

    def get(self, key):
        """Returns the value associated with the given key from the hashtable."""
        index = self._hash(key)
        if self._buckets[index] is None:
            return None
        for item in self._buckets[index]:
            if item[0] == key:
                return item[1]
        return None

