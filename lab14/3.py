class Restaurant:
    def __init__(self, a, b):
        self.restaurant_name = a
        self.cuisine_type = b
        self.number_served = 0  

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")

    def set_number_served(self, a):
        self.number_served = a

    def increment_number_served(self, b):
        self.number_served += b



a = Restaurant("La Piazza", "Italian")
b = Restaurant("Sakura", "Japanese")
c = Restaurant("Le Gourmet", "French")  


a.describe_restaurant()
b.describe_restaurant()
c.describe_restaurant()


a.set_number_served(50)
print(f"Number served: {a.number_served}")

a.increment_number_served(20)
print(f"Number served after increment: {a.number_served}")


class IceCreamStand(Restaurant):
    def __init__(self, a, b="Ice Cream"):
        super().__init__(a, b)
        self.flavors = []

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


a = IceCreamStand("Sweet Treats")
a.flavors = ["Vanilla", "Chocolate", "Strawberry"]
a.display_flavors()
