class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None

# Example usage:
if __name__ == "__main__":
    phone_book = HashTable(10)
    phone_book.put("John", "123-456-7890")
    phone_book.put("Alice", "987-654-3210")
    phone_book.put("Bob", "555-123-4567")

    print("John's phone number:", phone_book.get("John"))
    print("Alice's phone number:", phone_book.get("Alice"))
    print("Bob's phone number:", phone_book.get("Bob"))
