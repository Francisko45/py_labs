
class Pet:
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit(self)



class Cat(Pet):
    pass


class Dog(Pet):
    pass


class Parrot(Pet):
    pass



class Visitor:
    def visit(self, pet):
        raise NotImplementedError("This method should be overridden in a subclass")



class Veterinarian(Visitor):  
    def visit(self, pet):
        print(f"Veterinarian is treating {pet.name}.")


class Scoundrel(Visitor): 
    def visit(self, pet):
        print(f"Scoundrel is teasing {pet.name}.")


class Master(Visitor):  
    def visit(self, pet):
        print(f"Master is feeding {pet.name}.")


class Child(Visitor): 
    def visit(self, pet):
        print(f"Child is playing with {pet.name}.")



if __name__ == "__main__":
    a = Cat("Tom")  
    b = Dog("Rex")  

    
    veterinarian = Veterinarian()
    scoundrel = Scoundrel()
    master = Master()
    child = Child()

   
    for visitor in [veterinarian, scoundrel, master, child]:
        a.accept(visitor)
        b.accept(visitor)
