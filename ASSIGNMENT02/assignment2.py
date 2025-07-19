# in this assignment used sentinal node with doubly linkedlist

class Node:
    def __init__(self, data, next = None, prev = None) -> None:
        self.next = next
        self.prev = prev
        self.data = data

    def get_data(self):
        return self.data

class LinkedList:
    def __init__(self, front = None, back = None) -> None:
        self.front = front
        self.back = back
    
    def show(self):
        current = self.front
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("None")


    def get_front(self):
        return self.front
    
    def get_back(self):
        return self.back
    
    def insert_front(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
    
    def insert_back(self, data):
        new_node = Node(data)
        if self.back is None:
            self.back = self.front = new_node
        else:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node
 

    def insert(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.back = new_node
            return
           
        if data < self.front.data:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
            return
        
        if data >= self.back.data:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node
            return
        
        current = self.front
        while current is not None and current.data < data:
            current = current.next
        previous = current.prev
        previous.next = new_node
        new_node.prev = previous
        new_node.next = current
        current.prev = new_node
        
    def remove(self, data):
        current = self.front
        while current is not None and current.data != data:
            current = current.next
        
        if current is None:
            return False
        
        elif current == self.front:
            self.front = current.next
            self.front.prev = None
            return True
        elif current == self.back:
            self.back = current.prev
            self.back.next = None
            return True
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            return True

    def is_present(self, data):
        current = self.front
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False


    def __len__(self):
        count = 0
        current = self.front
        while current is not None:
            count += 1
            current = current.next
        return count

    
def main():
    test = LinkedList()
    
    test.insert(1)
    test.insert(3)
    test.insert(2)
    test.insert(5)
    test.insert(4)

    test.show()
    print(test.__len__())
    print(test.is_present(3))
    print(test.remove(3))
    print(test.remove(3))
    print(test.is_present(3))
    test.show()
    print(test.__len__())

main()
