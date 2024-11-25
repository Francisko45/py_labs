class LowerUp:
    def __init__(self):
        self.text = ""

    def get_input(self):
        """Отримує рядок з вводу консолі"""
        self.text = input("Введіть рядок: ")

    def print(self):
        """Друкує рядок у верхньому регістрі"""
        print(self.text.upper())

lower_up = LowerUp()
lower_up.get_input()
lower_up.print()
