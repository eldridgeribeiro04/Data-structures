class Array:
    
    def __init__(self, capacity=16):
        
        if capacity < 0:
            ValueError("Illegal capacity")
        
        self.capacity = capacity
        self.len = 0    #what we show users
        self.arr = [None] * capacity #what the actual capacity is
        
            
    def size(self):
        return self.len
    
    def is_empty(self):
        return self.len == 0
    
    def get(self, index):
        
        if index < 0 or index >= self.len:
            raise IndexError("Index out of bounds")
        return self.arr[index]
    
    def clear(self):
        for i in range(self.len):
            self.arr[i] = None
        self.len = 0
        
    def add(self, elem):
        if self.len + 1 >= self.capacity:
            if self.capacity == 0:
                self.capacity = 1
            else:
                self.capacity *= 2
                
            new_arr = [None] * self.capacity
            for i in range(self.len):
                new_arr[i] = self.arr[i]
        self.arr = new_arr
        
        self.arr[self.len] = elem
        self.len += 1

    def remove_at(self, index):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of bounds")
        
        self.capacity -= 1
        new_arr = [None] * self.capacity
        for i in range(self.len):
            if i == index:
                pass
            else:
                new_arr.append(self.arr[i])
        
        self.arr = new_arr
        self.len -= 1
        
    def remove(self, obj):
        index = self.index_of(obj)
        if index == -1:
            return False
        self.remove_at(index)
        return True
        
    def indexOf(self, obj):
        for i in range(self.len):
            if obj is None:
                if self.arr[i] is None:
                    return i
            else:
                if self.arr[i] == obj:
                    return self.arr[i]
            return -1
        
    def contains(self, obj):
        return self.index_of(obj) != -1
    
    def __iter__(self):
        for i in range(self.len):
            yield self.arr[i]
            
    def __str__(self):
        if self.len == 0:
            return "[]"
        else:
            return "[" + ",".join(str(self.arr[i]) for i in range(self.len)) + "]"
            