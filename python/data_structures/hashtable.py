class Hashtable:
    def __init__(self, size=100):
        self.size = size
        self._buckets = [[] for _ in range(self.size)]


    def set(self, key, value):
        index = self._hash(key)
        bucket = self._buckets[index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return None

    def has(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]
        for existing_key, _ in bucket:
            if existing_key == key:
                return True
        return False

    def keys(self):
        keys = []
        for bucket in self._buckets:
            for key, _ in bucket:
                keys.append(key)
        return keys

    def _hash(self, key):
        if isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        else:
            return hash(key) % self.size
