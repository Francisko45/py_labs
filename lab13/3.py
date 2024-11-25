import random

class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.gladness = 50
        self.money = 100
        self.alive = True

    def __str__(self):
        return f"Human's name is {self.name}"

    def work(self, job):
        print(f"{self.name} is working as a {job.title}.")
        self.money += job.salary
        self.gladness -= 5

    def chill(self, home):
        print(f"{self.name} is chilling at home.")
        self.gladness += 5
        self.money -= 10
        home.cleanliness -= 5

    def eat(self, home):
        print(f"{self.name} is eating at home.")
        self.gladness += 3
        self.money -= 5
        home.food -= 10

    def drive(self, car):
        print(f"{self.name} is driving the {car.brand}.")
        self.gladness -= 3
        car.fuel -= 10

    def is_alive(self):
        if self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.money <= 0:
            print("Bankrupt...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Money = {self.money}")

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.fuel = 100
        self.passengers = []  

    def add_passengers(self, *humans):
        for passenger in humans:
            self.passengers.append(passenger)

    def print_passengers_names(self):  
        if self.passengers: 
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")

    def refuel(self):
        print(f"{self.brand} is refueling.")
        self.fuel = 100

class Home:
    def __init__(self):
        self.food = 50
        self.cleanliness = 100

    def clean(self):
        print("Home is being cleaned.")
        self.cleanliness = 100

    def cook(self):
        print("Cooking food.")
        self.food -= 10

class Work:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary

Alex = Human("Alex")
Oleg = Human("Oleg")
Irina = Human("Irina")

car = Auto("Mercedes")
car.add_passengers(Alex, Oleg, Irina)
car.print_passengers_names()

home = Home()
job = Work(title="Engineer", salary=50)

for day in range(1, 366):
    if not Alex.alive and not Oleg.alive and not Irina.alive:
        break
    print(f"\nDay {day}:")
    
    for person in [Alex, Oleg, Irina]:
        if not person.alive:
            continue
        activity = random.choice(["work", "chill", "eat", "drive"])
        if activity == "work":
            person.work(job)
        elif activity == "chill":
            person.chill(home)
        elif activity == "eat":
            person.eat(home)
            home.cook()
        elif activity == "drive":
            person.drive(car)
            if car.fuel <= 10:
                car.refuel()

        person.end_of_day()
        person.is_alive()
