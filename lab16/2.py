from abc import ABC, abstractmethod


class Diagnosable(ABC):
    @abstractmethod
    def diagnose(self):
        pass


class Car:
    def __init__(self, model):
        self.model = model

class Human:
    def __init__(self, name):
        self.name = name

class Animal:
    def __init__(self, species):
        self.species = species


class DiagnosableCar(Car, Diagnosable):
    def diagnose(self):
        print(f"Diagnosing car {self.model}: Checking engine and tires.")

class DiagnosableHuman(Human, Diagnosable):
    def diagnose(self):
        print(f"Diagnosing human {self.name}: Checking vitals and symptoms.")

class DiagnosableAnimal(Animal, Diagnosable):
    def diagnose(self):
        print(f"Diagnosing animal {self.species}: Checking health.")


class Doctor(ABC):
    @abstractmethod
    def diagnose(self, patient):
        pass

class Surgeon(Doctor):
    def diagnose(self, patient):
        print(f"Surgeon is performing surgery on {patient.name if isinstance(patient, Human) else patient.species}.")

class Neurosurgeon(Surgeon):
    def diagnose(self, patient):
        print(f"Neurosurgeon is performing brain surgery on {patient.name if isinstance(patient, Human) else patient.species}.")


if __name__ == "__main__":
    
    car = DiagnosableCar("Toyota Corolla")
    human = DiagnosableHuman("John")
    animal = DiagnosableAnimal("Dog")

    
    car.diagnose()
    human.diagnose()
    animal.diagnose()

    
    surgeon = Surgeon()
    neurosurgeon = Neurosurgeon()

    
    surgeon.diagnose(human)
    neurosurgeon.diagnose(human)
    surgeon.diagnose(animal)
