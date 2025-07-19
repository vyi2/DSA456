    def insert(self, data):
        new_node = Node(data) #1
        if self.front is None: #1
            self.front = self.back = new_node #1 
            return #1 
           
        if data < self.front.data: #1
            new_node.next = self.front #1 
            self.front.prev = new_node #1
            self.front = new_node #1
            return #1
        
        if data >= self.back.data: #1
            new_node.prev = self.back #1
            self.back.next = new_node #1
            self.back = new_node #1
            return #1
        
        current = self.front #1
        while current is not None and current.data < data: #1n+1
            current = current.next
        previous = current.prev #1
        previous.next = new_node #1 
        new_node.prev = previous #1
        new_node.next = current #1
        current.prev = new_node #1

#T(n) = 1 + 1 + 1 + 1 + 1 + 1n + 1 + 1 + 1 + 1 + 1 + 1 
#= 11 + n
#T(n) = O(n)

def remove(self, data):
        current = self.front #1
        while current is not None and current.data != data: #1n+1
            current = current.next
        
        if current is None: #1
            return False #1
        
        elif current == self.front: #1 
            self.front = current.next #1
            self.front.prev = None #1
            return True #1
        elif current == self.back: #1
            self.back = current.prev #1
            self.back.next = None #1
            return True #1
        else: #1
            current.prev.next = current.next #1
            current.next.prev = current.prev #1
            return True #1

#T(n) = 1 + 1n + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
#= 9 + n
#T(n) = O(n)

def is_present(self, data):
        current = self.front #1
        while current is not None: #3n+1
            if current.data == data:
                return True
            current = current.next
        return False #1

#T(n) = 1 + 3n + 1 + 1 + 1
#= 3n + 4
#T(n) = O(n)

def __len__(self):
    count = 0 #1
    current = self.front #1 
    while current is not None: 3n+1
        count += 1
        current = current.next
    return count #1

T(n) = 1 + 1 + 3n + 1 + 1
#= 4 + 3n
#T(n) = O(n)