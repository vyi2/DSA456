class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.front = None
        self.back = None

    def insert(self, key, value):
        new_node = Node(key, value)
        if self.front is None:
            self.front = self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def find_node(self, key):
        current = self.front
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove(self, key):
        current = self.find_node(key)
        if current is None:
            return False
        if current == self.front:
            self.front = current.next
            if self.front:
                self.front.prev = None
        elif current == self.back:
            self.back = current.prev
            if self.back:
                self.back.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        return True

    def modify(self, key, value):
        node = self.find_node(key)
        if node:
            node.value = value
            return True
        return False


class ChainingTable:
    def __init__(self, capacity=32):
        self.table = [None] * capacity
        self.size = 0

    def _hash(self, key):
        return hash(key) % len(self.table)

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = LinkedList()

        bucket = self.table[index]
        if bucket.find_node(key):
            return False

        bucket.insert(key, value)
        self.size += 1

        # Resize
        if self.size > len(self.table):
            old_table = self.table
            new_capacity = len(old_table) * 2
            self.table = [None] * new_capacity
            self.size = 0

            for bucket in old_table:
                if bucket:
                    current = bucket.front
                    while current:
                        new_index = hash(current.key) % new_capacity
                        if self.table[new_index] is None:
                            self.table[new_index] = LinkedList()
                        self.table[new_index].insert(current.key, current.value)
                        self.size += 1
                        current = current.next
        return True

    def modify(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        if bucket is None:
            return False
        return bucket.modify(key, value)

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if bucket is None:
            return False
        removed = bucket.remove(key)
        if removed:
            self.size -= 1
        return removed

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if bucket is None:
            return None
        node = bucket.find_node(key)
        return node.value if node else None

    def capacity(self):
        return len(self.table)

    def __len__(self):
        return self.size


def main():
    ht = ChainingTable(4)

    print("Insert 1 (apple):", ht.insert(1, "apple"))  # True
    print("Insert 2 (date):", ht.insert(2, "pear"))  # True
    print("Insert 5 (banana):", ht.insert(5, "banana"))  # True
    print("Insert 9 (cherry):", ht.insert(9, "cherry"))  # True
    print("Capacity:", ht.capacity())  # 4

    print("\nDupe Insert (1, apple):", ht.insert(1, "apple"))  # False

    print("\n1:", ht.search(1))  # "apple"
    print("2:", ht.search(2))  # "pear"
    print("5:", ht.search(5))  # "banana"
    print("9:", ht.search(9))  # "cherry"
    print("10:", ht.search(10))  # None

    print("\nModify 2 blueberry:", ht.modify(2, "blueberry"))  # True
    print("Modify 6 banana:", ht.modify(6, "banana"))  # False
    print("2 after modify:", ht.search(2))  # "blueberry"

    print("\nRemove 9:", ht.remove(9))  # True
    print("Remove 7:", ht.remove(7))  # False
    print("Search 9 after removal:", ht.search(9))  # None

    print("\nCurrent size:", len(ht))  # 3

    print("\nInsert 6 grape:", ht.insert(6, "grape"))  # True
    print("Insert 7 tomato:", ht.insert(7, "tomato"))  # True

    print(f"New Capacity: {ht.capacity()}\n")  # 8

    for index in range(ht.capacity()):
        bucket = ht.table[index]
        if bucket:
            current = bucket.front
            while current:
                print(f"Index {current.key}: {current.value}")
                current = current.next
        else:
            print(f"Index {index}: Empty")


main()
