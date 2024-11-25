import random

class Cat:
    def __init__(self, name='Макркіз'):
        self.name = name
        self.favorite_toys = ['mouse'] 
        self.not_favorite_toys = ['dog']  

    def say_hello(self):
        print(f"{self.name} каже: Мяу!")

    def introduce_yourself(self):
        print(f"Привіт, я {self.name}. Мені подобається {len(self.favorite_toys)} іграшок і я не люблю {len(self.not_favorite_toys)} іграшок.")

    def like_toy(self, toy):
        if toy not in self.favorite_toys and toy not in self.not_favorite_toys:
            self.favorite_toys.append(toy)
            print(f"{self.name} тепер любить іграшку: {toy}.")

    def dislike_toy(self, toy):
        if toy in self.favorite_toys:
            self.favorite_toys.remove(toy)
        if toy not in self.not_favorite_toys:
            self.not_favorite_toys.append(toy)
        print(f"{self.name} тепер не любить іграшку: {toy}.")

    def check_and_add_toy(self, toy):
        action = random.choice(['like', 'dislike', 'ignore'])
        if action == 'like':
            self.like_toy(toy)
        elif action == 'dislike':
            self.dislike_toy(toy)
        else:
            print(f"{self.name} ігнорує іграшку: {toy}.")


def simulate_cat_walk(a, b, iterations=10):
    for i in range(iterations):
        toy = random.choice(b)  
        print(f"\nІтерація {i+1}:")
        a.check_and_add_toy(toy)

    a.introduce_yourself()


a = Cat(name="Маркіз")


b = ['mouse', 'ball', 'string', 'dog', 'rat', 'bird']


simulate_cat_walk(a, b)
