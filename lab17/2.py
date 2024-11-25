class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0 
    
    def __next__(self):
        if self.index < len(self.collection):
            value = self.collection[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration  


class Iterable:
    
    def __init__(self):
        self.container = []  
    
    def append(self, value):
        self.container.append(value)
    
    def __iter__(self):
        return Iterator(self.container)



my_collection = Iterable()


my_collection.append(10)
my_collection.append(20)
my_collection.append(30)


for item in my_collection:
    print(item)
