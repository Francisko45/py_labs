class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.cursor = 0  
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cursor < len(self.collection):
            value = self.collection[self.cursor]
            self.cursor += 1
            return value
        else:
            raise StopIteration  



my_list = [1, 2, 3, 4, 5]


iterator = Iterator(my_list)


for item in iterator:
    print(item)


for item in iterator:
    print(item)  
