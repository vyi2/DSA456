def insert(self, key, value):
    if self.search(key) != None: # n
        return False

    if len(self) == self.cap: # 1
        new_table = [None for i in range(self.cap * 2)] # n

        for i in range(self.cap): # n
            new_table[i] = self.the_table[i] # 1

        self.the_table = new_table # 1
        self.cap *= 2 # 1

    self.the_table[len(self)] = self.Record(key, value) # 1
    size = len(self) # 1

    for i in range(0, size - 1): # n(n-1)/2
        for j in range(0, size - 1 - i):
            if self.the_table[j].key > self.the_table[j + 1].key:
                tmp = self.the_table[j]
                self.the_table[j] = self.the_table[j + 1]
                self.the_table[j + 1] = tmp

    return True # 1

#T(n) = n + 1 + n + n + 1 + 1 + 1 + 1 + 1 n(n-1)/2 * (1 + 1 + 1 + 1)
#= 3n + 6 + n(n-1)/2 * 4
#= 3n + 6 + 2n(n-1)
#= 3n - 2n + 6 + 2n^2
#= n + 6 + 2n^2
#T(n) = O(n^2)


def modify(self, key, value):
    
    i = 0  # 1
    while i < len(self) and self.the_table[i].key != key:  # n
        i += 1  # 1
    if i == len(self):  # 1
        return False  # 1
    else:
        self.the_table[i].value = value  # 1
        return True  # 1

#T(n) = 1 + n * (1 + 1) + 1 + 1 + 1 + 1
#= 1 + n * 2 + 4
#= 1 + 2n + 4
#= 2n + 5
#T(n) = O(n)
