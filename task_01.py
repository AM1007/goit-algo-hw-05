# Define a class for a hash table
class HashTable:

    # Constructor for the HashTable class
    def __init__(self, size):
        # Set the size of the hash table
        self.size = size
        # Create an empty list to store the hash table
        self.table = [[] for _ in range(self.size)]

    # Define a hash function to map keys to indices of the hash table
    def hash_function(self, key):
        # Use the built-in hash function to generate a hash value for the key
        hash_value = hash(key)
        # Modulo the hash value by the size of the hash table to get the index
        key_hash = hash_value % self.size
        # Return the index
        return key_hash

    # Insert a key-value pair into the hash table
    def insert(self, key, value):
        # Generate the hash value for the key
        key_hash = self.hash_function(key)
        # Create a list to store the key-value pair
        key_value = [key, value]

        # Check if the key already exists in the hash table
        for pair in self.table[key_hash]:
            if pair[0] == key:
                # If the key exists, update the value
                pair[1] = value
                return True

        # If the key doesn't exist, add the key-value pair to the hash table
        self.table[key_hash].append(key_value)
        return True

    # Retrieve the value associated with a key from the hash table
    def get(self, key):
        # Generate the hash value for the key
        key_hash = self.hash_function(key)

        # Check if the key exists in the hash table
        for pair in self.table[key_hash]:
            if pair[0] == key:
                # If the key exists, return the value
                return pair[1]

        # If the key doesn't exist, return None
        return None

    # Delete a key-value pair from the hash table
    def delete(self, key):
        # Generate the hash value for the key
        key_hash = self.hash_function(key)

        # Check if the key exists in the hash table
        for i, pair in enumerate(self.table[key_hash]):
            if pair[0] == key:
                # If the key exists, remove the key-value pair from the hash table
                self.table[key_hash].pop(i)
                return True

        # If the key doesn't exist, return False
        return False

# Example usage of the HashTable class
H = HashTable(5)

# Insert key-value pairs into the hash table
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

# Retrieve the values associated with the keys
print(H.get("apple")) # Output: 10
print(H.get("orange")) # Output: 20
print(H.get("banana")) # Output: 30

# Delete the key-value pair with the key "orange"
H.delete("orange")

# Retrieve the value associated with the key "orange"
print(H.get("orange")) # Output: None, since the key-value pair was deleted