class FibonacciGenerator:
    def __init__(self, n):
        self.n = n  
        self.a, self.b = 0, 1  
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a > self.n:
            raise StopIteration 
        
        current = self.a 
        self.a, self.b = self.b, self.a + self.b  
        return current  


gen = FibonacciGenerator(100)

for num in gen:
    print(num)
