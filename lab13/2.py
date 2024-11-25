import random
import time

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100 
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 10
        self.progress -= 0.1
        self.money -= 10  

    def to_work(self):
        print("Time to work")
        self.money += 20
        self.gladness -= 5
        self.progress -= 0.05

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.money < 0:
            print("Bankrupt...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = f"Day {day} of {self.name}'s life"
        print(f"{day:=^50}")
        if self.money < 20:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        elif self.gladness < 30:
            self.to_chill()
        elif self.gladness > 30 and self.progress < 2:
            self.to_study()
        elif self.gladness > 30 and self.money < 50:
            self.to_work()
        else:
            live_cube = random.randint(1, 3)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()

        self.end_of_day()
        self.is_alive()

nick = Student(name="Igor")
for day in range(1, 366):
    if not nick.alive:
        break
    time.sleep(0.2)
    nick.live(day)
