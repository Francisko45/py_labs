class FactorialGenerator:
    def __init__(self, n):
        self.n = n  
        self.k = 1  
        self.f = 1  
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.k > self.n:
            raise StopIteration 
        
        self.f *= self.k  
        self.k += 1 
        return self.f 


gen = FactorialGenerator(5)


for fact in gen:
    print(fact)
