import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0

        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n
    
    def append(self, item):
        if self.n == self.size:
            #resize
            self.__resize(self.size*2)
        
        #append
        self.A[self.n] = item
        self.n += 1

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ","

        return '[' + result[:-1] + ']'

    def __make_array(self, capacity):
        return (capacity*ctypes.py_object)()