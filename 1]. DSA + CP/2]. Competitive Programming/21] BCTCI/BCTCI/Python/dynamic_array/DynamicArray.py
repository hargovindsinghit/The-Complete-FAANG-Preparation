class DynamicArray:
    def __init__(self):
        self._size = 0
        self._capacity = 10
        self._array = [None] * self._capacity
    
    def append(self, value):
        if self._size == self._capacity:
            self._resize()
        self._array[self._size] = value
        self._size += 1

    def _resize(self):
        self._capacity *= 2
        new_array = [None] * self._capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]
    
    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        self._array[index] = value

    def __len__(self):
        return self._size
    
    def __str__(self):
        return str(self._array[:self._size])
    
    def __repr__(self):
        return str(self)

    def __iter__(self):
        for i in range(self._size):
            yield self._array[i]
    
    def __contains__(self, value):
        for i in range(self._size):
            if self._array[i] == value:
                return True
        return False
    
    def index(self, value):
        for i in range(self._size):
            if self._array[i] == value:
                return i
        raise ValueError("Value not found")
    
    def remove(self, value):
        for i in range(self._size):
            if self._array[i] == value:
                for j in range(i, self._size - 1):
                    self._array[j] = self._array[j + 1]
                self._size -= 1
                return
        raise ValueError("Value not found")
    

if __name__ == "__main__":
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
    print(arr)
    print(len(arr))
    print(arr[5])
    arr[5] = 100
    print(arr)
    print(100 in arr)
    print(1000 in arr)
    print(arr.index(100))
    arr.remove(100)
    print(arr)
    arr.remove(100)
    print(arr)
