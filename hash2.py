class TelephoneBook:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash1(self, key):
        return hash(key) % self.size

    def hash2(self, key):
        return 7 - (hash(key) % 7)

    def insert(self, name, number):
        index = self.hash1(name)
        step_size = self.hash2(name)
        original_index = index

        while self.table[index] is not None:
            index = (index + step_size) % self.size
            if index == original_index:
                print("Table is full. Cannot insert:", name)
                return

        self.table[index] = (name, number)
        print("Inserted:", name)

    def search(self, name):
        index = self.hash1(name)
        step_size = self.hash2(name)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == name:
                print("Found:", name, "-", self.table[index][1])
                return
            index = (index + step_size) % self.size
            if index == original_index:
                break

        print("Not found:", name)

    def display(self):
        print("\nTelephone Book:")
        for entry in self.table:
            if entry is not None:
                print(entry[0], "-", entry[1])

def main():
    size = int(input("Enter the size of the hash table: "))
    telephone_book = TelephoneBook(size)

    while True:
        print("\nMenu:")
        print("1. Insert a new entry")
        print("2. Search for an entry")
        print("3. Display the telephone book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name: ")
            number = input("Enter the number: ")
            telephone_book.insert(name, number)
        elif choice == '2':
            name = input("Enter the name to search: ")
            telephone_book.search(name)
        elif choice == '3':
            telephone_book.display()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
